package bloomfilter

import (
	"encoding/binary"
	"math"
)

type BloomFilter struct {
	m                uint64
	k                uint64
	numberOfElements uint64
	hashes           []HashWithSeed
	data             []uint64
}


func NewBloomFilter(expectedElements int, falsePositiveRate float64) BloomFilter {
	var bloomfilter BloomFilter
	bloomfilter.m = uint64(CalculateM(expectedElements, falsePositiveRate))
	bloomfilter.k = uint64(CalculateK(expectedElements, uint(bloomfilter.m)))
	bloomfilter.hashes = CreateHashFunctions(uint32(bloomfilter.k))
	bloomfilter.numberOfElements = uint64(math.Ceil(float64(float64(bloomfilter.m) / 64)))
	bloomfilter.m = bloomfilter.numberOfElements * 64
	bloomfilter.data = make([]uint64, bloomfilter.numberOfElements)
	return bloomfilter
}

func (bl *BloomFilter) Insert(data []byte) {
	for i := uint64(0); i < bl.k; i++ {
		var h uint64 = bl.hashes[i].Hash(data)
		elementIndex, elementBit := bl.calculateIndecies(h)
		var mask uint64 = (1 << elementBit)
		bl.data[elementIndex] |= mask
	}
}

func (bl *BloomFilter) IsNotIn(data []byte) bool {
	for i := uint64(0); i < bl.k; i++ {
		var h uint64 = bl.hashes[i].Hash(data)
		elementIndex, elementBit := bl.calculateIndecies(h)
		var mask uint64 = (1 << elementBit)
		if bl.data[elementIndex]&mask == 0 {
			return true
		}
	}
	return false
}

func (bl *BloomFilter) calculateIndecies(hash uint64) (uint64, uint8) {
	var index uint64 = hash % bl.m
	var elementIndex uint64 = index / 64
	var elementBit uint8 = uint8(index % 64)

	return elementIndex, elementBit
}

func (bl *BloomFilter) Serialize() []byte {
	// 1B - Version
	// 8B - m
	// 8B - k
	// 8B - number of elements
	// k*4B - hash seeds
	// nofEl * 8B - podaci
	const CURRENT_VERSION uint8 = 1

	var result []byte = []byte{CURRENT_VERSION} // verzija

	// m
	var mBytes []byte = make([]byte, 8)
	binary.BigEndian.PutUint64(mBytes, bl.m)
	result = append(result, mBytes...)

	// k
	var kBytes []byte = make([]byte, 8)
	binary.BigEndian.PutUint64(kBytes, bl.k)
	result = append(result, kBytes...)

	// number of elements
	var numOfElemBytes []byte = make([]byte, 8)
	binary.BigEndian.PutUint64(numOfElemBytes, bl.numberOfElements)
	result = append(result, numOfElemBytes...)

	// k hash seeds
	for i := uint64(0); i < bl.k; i++ {
		result = append(result, bl.hashes[i].Seed...)
	}

	// elements
	for i := uint64(0); i < bl.numberOfElements; i++ {
		var elementBytes []byte = make([]byte, 8)
		binary.BigEndian.PutUint64(elementBytes, bl.data[i])
		result = append(result, elementBytes...)
	}
	return result
}

func (bl *BloomFilter) Deserialize(data []byte)  {
	// 1B - Version
	// 8B - m
	// 8B - k
	// 8B - number of elements
	// k*4B - hash seeds
	// nofEl * 8B - podaci
	const CURRENT_VERSION uint8 = 1
	var version uint8 = uint8(data[0])
	if version != CURRENT_VERSION {
		// handle diffrent version
		return
	}
	// m
	data = data[1:]
	var mBytes []byte = data[:8]
	bl.m = binary.BigEndian.Uint64(mBytes)
	data = data[8:]
	// k
	var kBytes []byte = data[:8]
	bl.k = binary.BigEndian.Uint64(kBytes)
	data = data[8:]

	// number of elements

	var numOfElemBytes []byte = data[:8]
	bl.numberOfElements = binary.BigEndian.Uint64(numOfElemBytes)
	data = data[8:]


	// seeds
	bl.hashes = make([]HashWithSeed, bl.k)
	for i := uint64(0); i < bl.k; i++ {
		var seedBytes []byte = data[:4]
		bl.hashes[i] = HashWithSeed{seedBytes}
		data = data[4:]
	}
	// podaci
	bl.data = make([]uint64, bl.numberOfElements)
	for i := uint64(0); i < bl.numberOfElements; i++ {
		var elementBytes []byte = data[:8]
		bl.data[i] = binary.BigEndian.Uint64(elementBytes)
		data = data[8:]
	}
}