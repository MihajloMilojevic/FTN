
export default async function validateImageUrl(url) { 
    try {
        const res = await fetch(url);
        const buff = await res.blob();
        return buff.type.startsWith('image/')
    }
    catch {
        return false;
    }
}