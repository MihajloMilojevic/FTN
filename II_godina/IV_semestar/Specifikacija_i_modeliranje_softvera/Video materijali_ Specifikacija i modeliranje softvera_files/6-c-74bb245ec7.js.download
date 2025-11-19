(window["canvasWebpackJsonp"]=window["canvasWebpackJsonp"]||[]).push([[6],{"3Zzb":function(e,t,n){"use strict"
n.d(t,"a",(function(){return w}))
var o=n("1OyB")
var i=n("vuIU")
var r=n("Ji7U")
var a=n("LK+K")
var s=n("q1tI")
var u=n.n(s)
var c=n("17x9")
var l=n.n(c)
var f=n("i8i4")
var h=n.n(f)
var d=n("AdN2")
var v=n("VTBJ")
var p=n("Ff2n")
var m=n("jtGx")
var b=n("FOOe")
var y,O,_,N
var g=(y=Object(b["a"])(),y(O=(N=_=function(e){Object(r["a"])(n,e)
var t=Object(a["a"])(n)
function n(e){var i
Object(o["a"])(this,n)
i=t.call(this,e)
i.state={mountNode:i.findMountNode(e)}
return i}Object(i["a"])(n,[{key:"componentDidMount",value:function(){this.props.open&&"function"===typeof this.props.onOpen&&this.props.onOpen(this.DOMNode)}},{key:"componentDidUpdate",value:function(e){var t=this.findMountNode(this.props)
t!==this.state.mountNode&&this.setState({mountNode:t})
this.props.open&&!e.open&&"function"===typeof this.props.onOpen&&this.props.onOpen(this.DOMNode)
!this.props.open&&e.open&&"function"===typeof this.props.onClose&&this.props.onClose()}},{key:"componentWillUnmount",value:function(){this.removeNode()
this.props.open&&"function"===typeof this.props.onClose&&this.props.onClose()}},{key:"render",value:function(){var e=this.props.children
return this.props.open&&u.a.Children.count(e)>0?h.a.createPortal(e,this.insertNode()):null}},{key:"removeNode",value:function(){if(this.DOMNode&&this.DOMNode.parentNode&&"function"===typeof this.DOMNode.parentNode.removeChild){this.DOMNode.parentNode.removeChild(this.DOMNode)
this.DOMNode=null
this.props.elementRef(this.DOMNode)}}},{key:"insertNode",value:function(){var e=this.props,t=(e.open,e.insertAt),n=(e.onOpen,e.onClose,e.mountNode,e.children,e.elementRef),o=Object(p["a"])(e,["open","insertAt","onOpen","onClose","mountNode","children","elementRef"])
if(!this.DOMNode){var i=document.createElement("span")
var r=Object(v["a"])({},Object(m["b"])(o),{dir:this.dir})
Object.keys(r).forEach((function(e){i.setAttribute(e,r[e])}))
n(i)
this.DOMNode=i}this.DOMNode.parentNode!==this.state.mountNode&&("bottom"===t?this.state.mountNode.appendChild(this.DOMNode):this.state.mountNode.insertBefore(this.DOMNode,this.state.mountNode.firstChild))
return this.DOMNode}},{key:"findMountNode",value:function(e){var t
"function"===typeof e.mountNode?t=e.mountNode():e.mountNode&&(t=e.mountNode)
t&&t.nodeName||(t=document.body)
return t}},{key:"node",get:function(){return this.DOMNode}}])
n.displayName="ReactPortal"
return n}(u.a.Component),_.propTypes={open:l.a.bool,onOpen:l.a.func,onClose:l.a.func,mountNode:l.a.oneOfType([d["a"],l.a.func]),insertAt:l.a.oneOf(["bottom","top"]),children:l.a.node,elementRef:l.a.func},_.defaultProps={open:false,insertAt:"bottom",onOpen:function(e){},onClose:function(){},mountNode:void 0,children:null,elementRef:function(e){}},N))||O)
var E=n("0mOT")
var k,D,C,j
var R=(k=Object(b["a"])(),k(D=(j=C=function(e){Object(r["a"])(n,e)
var t=Object(a["a"])(n)
function n(){Object(o["a"])(this,n)
return t.apply(this,arguments)}Object(i["a"])(n,[{key:"componentDidMount",value:function(){this.renderPortal(this.props)}},{key:"shouldComponentUpdate",value:function(e,t){return!(Object(E["a"])(this.props,e)&&Object(E["a"])(this.state,t))}},{key:"componentWillReceiveProps",value:function(e){this.renderPortal(e)}},{key:"componentWillUnmount",value:function(){this.removePortal(this.props)}},{key:"render",value:function(){return null}},{key:"renderPortal",value:function(e){var t=this
var n=e.open,o=e.insertAt,i=e.onOpen,r=(e.onClose,e.elementRef),a=e.children,s=Object(p["a"])(e,["open","insertAt","onOpen","onClose","elementRef","children"])
var c=!this.DOMNode
var l=this.mountNode
var f=a
"string"===typeof f&&f.length>0&&(f=u.a.createElement("span",null,f))
if(n&&u.a.Children.count(f)>0){if(!this.DOMNode){var d=document.createElement("span")
var b=Object(v["a"])({},Object(m["b"])(s),{dir:this.dir})
Object.keys(b).forEach((function(e){d.setAttribute(e,b[e])}))
r(d)
this.DOMNode=d}this.DOMNode.parentNode!==l&&("bottom"===o?l.appendChild(this.DOMNode):l.insertBefore(this.DOMNode,l.firstChild))
var y=function(){(c||!t.props.open&&n)&&"function"===typeof i&&i(t.DOMNode)}
h.a.unstable_renderSubtreeIntoContainer(this,f,this.DOMNode,y)}else this.removePortal(e)}},{key:"removePortal",value:function(e){var t
if(this.DOMNode){t=h.a.unmountComponentAtNode(this.DOMNode)
this.DOMNode.parentNode&&this.DOMNode.parentNode.removeChild(this.DOMNode)
this.DOMNode=null
this.props.elementRef(this.DOMNode)}t&&"function"===typeof e.onClose&&e.onClose()}},{key:"mountNode",get:function(){var e
"function"===typeof this.props.mountNode?e=this.props.mountNode():this.props.mountNode&&(e=this.props.mountNode)
e&&e.nodeName||(e=document.body)
return e}},{key:"DOMNode",get:function(){return this._node},set:function(e){this._node=e}},{key:"node",get:function(){return this.DOMNode}}])
n.displayName="SubtreePortal"
return n}(s["Component"]),C.propTypes={open:l.a.bool,onOpen:l.a.func,onClose:l.a.func,mountNode:l.a.oneOfType([d["a"],l.a.func]),insertAt:l.a.oneOf(["bottom","top"]),children:l.a.node,elementRef:l.a.func},C.defaultProps={open:false,insertAt:"bottom",onOpen:function(e){},onClose:function(){},mountNode:null,children:null,elementRef:function(e){}},j))||D)
var F="function"===typeof h.a.createPortal
var w=function(e){Object(r["a"])(n,e)
var t=Object(a["a"])(n)
function n(){var e
Object(o["a"])(this,n)
for(var i=arguments.length,r=new Array(i),a=0;a<i;a++)r[a]=arguments[a]
e=t.call.apply(t,[this].concat(r))
e.handleElementRef=function(t){if(t){e.DOMNode=t
"function"===typeof e.props.elementRef&&e.props.elementRef(t)}}
return e}Object(i["a"])(n,[{key:"render",value:function(){return F?u.a.createElement(g,Object.assign({},this.props,{elementRef:this.handleElementRef})):u.a.createElement(R,Object.assign({},this.props,{elementRef:this.handleElementRef}))}}])
n.displayName="Portal"
return n}(s["Component"])
w.propTypes={open:l.a.bool,onOpen:l.a.func,onClose:l.a.func,mountNode:l.a.oneOfType([d["a"],l.a.func]),insertAt:l.a.oneOf(["bottom","top"]),children:l.a.node,elementRef:l.a.func}
w.defaultProps={open:false,insertAt:"bottom",onOpen:function(e){},onClose:function(){},mountNode:null,children:null,elementRef:function(e){}}},AdN2:function(e,t,n){"use strict"
n.d(t,"a",(function(){return a}))
var o=n("17x9")
var i=n.n(o)
var r=!!("undefined"!==typeof window&&window.document&&window.document.createElement)
var a=r?i.a.oneOfType([i.a.element,i.a.instanceOf(Element)]):i.a.element},EgqM:function(e,t,n){"use strict"
n.d(t,"a",(function(){return s}))
var o=n("QF4Q")
var i=n("i/8D")
function r(e,t){var n=Object(o["a"])(e)
var i=Object(o["a"])(t)
return!(!n||!i)&&(n.contains?n.contains(i):n.compareDocumentPosition?n===i||!!(16&n.compareDocumentPosition(i)):a(n,i))}function a(e,t){var n=t
while(n){if(n===e)return true
n=n.parentNode}return false}var s=i["a"]?r:a},ISHz:function(e,t,n){"use strict"
n.d(t,"a",(function(){return i}))
var o=n("i/8D")
var i=function(){var e
if(o["a"]&&window.requestAnimationFrame&&window.cancelAnimationFrame)e=function(e){var t=window.requestAnimationFrame(e)
return{cancel:function(){return window.cancelAnimationFrame(t)}}}
else{var t=(new Date).getTime()
e=function(e){var n=(new Date).getTime()
var o=Math.max(0,16-(n-t))
var i=setTimeout(e,o)
t=n
return{cancel:function(){return clearTimeout(i)}}}}return e}()},"K7t/":function(e,t,n){"use strict"
n.d(t,"a",(function(){return a}))
var o=n("QF4Q")
var i=n("EgqM")
var r=n("pgSO")
function a(e){var t=e&&Object(o["a"])(e)
var n=Object(r["a"])()
return t&&(n===t||Object(i["a"])(t,n))}},TjLr:function(e,t,n){"use strict"
n.d(t,"a",(function(){return a}))
var o=n("1OyB")
n("DEX3")
var i=n("lxKu")
var r=[]
var a=function e(){Object(o["a"])(this,e)}
a.focusRegion=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{}
var n
n="string"===typeof t?a.getEntry(e,t):a.addEntry(e,t)
if(n&&n.region&&"function"===typeof n.region.focus){n.region.focus()
return n.region}"[FocusRegionManager] Could not focus region with element: ".concat(e)}
a.activateRegion=function(e,t){var n=a.addEntry(e,t),o=n.region
return o}
a.getActiveEntry=function(){return r.find((function(e){var t=e.region
return t.focused}))}
a.findEntry=function(e,t){var n
n=t?r.findIndex((function(e){return e.id===t})):r.findIndex((function(t){return t.element===e}))
return n}
a.getEntry=function(e,t){return r[a.findEntry(e,t)]}
a.addEntry=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{}
var n=new i["a"](e,t)
var o=a.getActiveEntry()
var s=n.keyboardFocusable
r.forEach((function(e){var t=e.region
t&&t.deactivate(t.focused&&!s&&{keyboard:false})}))
n.activate()
t.shouldFocusOnOpen&&n.focus()
var u={id:n.id,element:e,region:n,children:[],parent:o}
r.push(u)
o&&o.children.push(u)
return u}
a.removeEntry=function(e,t){var n=a.findEntry(e,t)
var o=r[n]
n>-1&&r.splice(n,1)
return o}
a.isFocused=function(e,t){var n=a.getActiveEntry()
return t?n&&n.region&&n.id===t:n&&n.region&&n.element===e}
a.clearEntries=function(){r=[]}
a.blurRegion=function(e,t){var n=a.removeEntry(e,t)
if(n){var o=n.children,i=n.region,r=n.parent
i&&i.deactivate()
o&&o.forEach((function(e){var t=e.id,n=e.element
var o=a.removeEntry(n,t)
o&&o.region&&o.region.deactivate()}))
r&&r.region&&r.region.activate()
i&&i.blur()}}},"j+mt":function(e,t,n){"use strict"
n.d(t,"a",(function(){return u}))
var o=n("QF4Q")
var i=n("no2R")
var r=n("K7t/")
var a=n("pgSO")
var s=n("/UXv")
function u(e,t,n){var u=Object(o["a"])(e)
var c=Object(i["a"])(u)
if(!c.length){t.preventDefault()
return}if(Object(r["a"])(e)){var l=Object(a["a"])();-1===c.indexOf(l)&&c.push(l)}var f=c[t.shiftKey?0:c.length-1]
var h=Object(s["a"])(f)||Object(s["a"])(u)||!Object(r["a"])(e)
if(!h)return
if("function"===typeof n){n()
return}t.preventDefault()
var d=c[t.shiftKey?c.length-1:0]
d.focus()}},lxKu:function(e,t,n){"use strict"
n.d(t,"a",(function(){return g}))
var o=n("1OyB")
var i=n("vuIU")
n("DEX3")
var r=n("3zPy")
var a=n.n(r)
var s=n("EgqM")
var u=n("DUTp")
var c=n("yfCu")
function l(e){try{return e.contentDocument||e.contentWindow.document}catch(e){return null}}var f=n("no2R")
var h=n("BTe1")
var d=function(){function e(t){var n=this
var i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{shouldContainFocus:true,liveRegion:[]}
Object(o["a"])(this,e)
this._observer=null
this._attributes=[]
this._nodes=[]
this._parents=[]
this.handleDOMMutation=function(e){e.forEach((function(e){var t=Array.from(e.addedNodes)
var o=Array.from(e.removedNodes)
n.hideNodes(t)
o.forEach((function(e){"iframe"!==e.tagName.toLowerCase()&&n.restoreNode(e)
var t=n.parseIframeBodies(e)
t.forEach((function(e){n.restoreNode(e)}))}))}))}
var r="function"===typeof i.liveRegion?i.liveRegion():i.liveRegion
this._liveRegion=Array.isArray(r)?r:[r]
this._contextElement=t
this._options=i}Object(i["a"])(e,[{key:"updateElement",value:function(e){this._contextElement=e}},{key:"muteNode",value:function(e){var t=this
if(e&&"script"!==e.tagName.toLowerCase()){["role","aria-label","aria-hidden"].forEach((function(n){var o=e.getAttribute(n)
if(null!==o){t._attributes.push([e,n,o])
e.removeAttribute(n)}}))
this._observer.observe(e,{childList:true})}}},{key:"hideNodes",value:function(e){var t=this
e.forEach((function(e){var n
var o="function"===typeof e.getAttribute&&(null===(n=e.getAttribute("aria-live"))||void 0===n?void 0:n.toLowerCase())
if(e&&1===e.nodeType&&"script"!==e.tagName.toLowerCase()&&"assertive"!==o&&"polite"!==o&&-1===t._parents.indexOf(e)&&-1===t._nodes.indexOf(e)&&-1===t._liveRegion.indexOf(e)&&!t._contextElement.contains(e)){"iframe"!==e.tagName.toLowerCase()&&t.hideNode(e)
var i=t.parseIframeBodies(e)
i.forEach((function(e){t.hideNode(e)}))}}))}},{key:"hideNode",value:function(e){if("true"!==e.getAttribute("aria-hidden")){e.setAttribute("aria-hidden","true")
this._nodes.push(e)}}},{key:"restoreNode",value:function(e){var t=this._nodes.indexOf(e)
if(t>=0){e.removeAttribute("aria-hidden")
this._nodes.splice(t,1)}}},{key:"parseIframeBodies",value:function(e){if(!e)return[]
var t=[]
"iframe"===e.tagName.toLowerCase()?t.push(e):e.getElementsByTagName&&(t=Array.from(e.getElementsByTagName("iframe")))
return t.map((function(e){var t=null
try{t=e.contentDocument.body}catch(e){"[ui-a11y] could not find a document for iframe: ".concat(e)}return t})).filter((function(e){return null!==e}))}},{key:"activate",value:function(){if(!this._options.shouldContainFocus)return
this._observer=new MutationObserver(this.handleDOMMutation)
var e=this._contextElement
while(e&&1===e.nodeType&&"body"!==e.tagName.toLowerCase()){var t=e.parentElement
if(t){this._parents.push(t)
this.muteNode(t)
this.hideNodes(Array.prototype.slice.call(t.childNodes))}e=e.parentNode}}},{key:"deactivate",value:function(){if(this._observer){this._observer.disconnect()
this._observer=null}this._nodes.forEach((function(e){e.removeAttribute("aria-hidden")}))
this._nodes=[]
this._attributes.forEach((function(e){e[0].setAttribute(e[1],e[2]||"")}))
this._attributes=[]
this._parents=[]}}])
return e}()
var v=n("ISHz")
var p=n("K7t/")
var m=n("QF4Q")
var b=n("kR0I")
var y=n("gpCx")
var O=n("pgSO")
var _=n("j+mt")
var N=function(){function e(t,n){var i=this
Object(o["a"])(this,e)
this._contextElement=null
this._focusLaterElement=null
this._needToFocus=false
this._listeners=[]
this._raf=[]
this._active=false
this.handleDismiss=function(e){i._options.onDismiss(e)}
this.handleKeyDown=function(e){e.keyCode===a.a.codes.tab&&Object(_["a"])(i._contextElement,e)}
this.handleClick=function(e){i._wasDocumentClick=true}
this.handleWindowBlur=function(e){if(i._wasDocumentClick){i._wasDocumentClick=false
return}i._needToFocus=true}
this.handleFocus=function(e){if(i._needToFocus){i._needToFocus=false
if(!i._contextElement)return
i._raf.push(Object(v["a"])((function(){if(Object(p["a"])(i._contextElement))return
i.focusDefaultElement()})))}}
this.handleFirstTabbableKeyDown=function(e){e.keyCode===a.a.codes.tab&&e.shiftKey&&i._options.onBlur(e)}
this.handleLastTabbableKeyDown=function(e){e.keyCode!==a.a.codes.tab||e.shiftKey||i._options.onBlur(e)}
this._contextElement=Object(m["a"])(t)
this._options=n||{shouldContainFocus:true,shouldReturnFocus:true,onBlur:function(e){},onDismiss:function(e){},defaultFocusElement:null}
this._options.shouldReturnFocus&&(this._focusLaterElement=this.activeElement)}Object(i["a"])(e,[{key:"updateElement",value:function(e){this._contextElement=Object(m["a"])(e)}},{key:"focusDefaultElement",value:function(){var e=this.defaultFocusElement,t=this.shouldContainFocus
e?e.focus():t&&this.activeElement.blur()}},{key:"focus",value:function(){var e=this
if(this.focused)return
this._raf.push(Object(v["a"])((function(){e.focusDefaultElement()})))}},{key:"blur",value:function(){if(this._options.shouldReturnFocus&&this._focusLaterElement){try{this._focusLaterElement.focus()}catch(e){"\n          [KeyboardFocusRegion] You tried to return focus to ".concat(this._focusLaterElement,"\n          but it is not in the DOM anymore: ").concat(e,"\n          ")}this._focusLaterElement=null}}},{key:"activate",value:function(){var e=this.defaultFocusElement,t=this.shouldContainFocus
if(!this._active&&(e||t)){if(t)this._listeners.push(Object(c["a"])(this.doc,"keydown",this.handleKeyDown))
else{this._listeners.push(Object(c["a"])(this.firstTabbable||e,"keydown",this.handleFirstTabbableKeyDown))
this._listeners.push(Object(c["a"])(this.lastTabbable||e,"keydown",this.handleLastTabbableKeyDown))}this._listeners.push(Object(c["a"])(this.doc,"click",this.handleClick,true))
this._listeners.push(Object(c["a"])(this.win,"blur",this.handleWindowBlur,false))
this._listeners.push(Object(c["a"])(this.doc,"focus",this.handleFocus,true))
this._active=true}}},{key:"deactivate",value:function(){if(this._active){this._listeners.forEach((function(e){e.remove()}))
this._listeners=[]
this._raf.forEach((function(e){return e.cancel()}))
this._raf=[]
this._preventCloseOnDocumentClick=false
this._active=false}}},{key:"focused",get:function(){return Object(p["a"])(this._contextElement)}},{key:"shouldContainFocus",get:function(){var e=this._options.shouldContainFocus
return true===e||Array.isArray(e)&&e.includes["keyboard"]}},{key:"focusable",get:function(){return Object(b["a"])(this._contextElement,(function(){return true}),true)||[]}},{key:"tabbable",get:function(){return Object(f["a"])(this._contextElement)||[]}},{key:"firstTabbable",get:function(){return this.tabbable[0]}},{key:"lastTabbable",get:function(){return this.tabbable.pop()}},{key:"firstFocusable",get:function(){return this.focusable[0]}},{key:"lastFocusable",get:function(){return this.focusable.pop()}},{key:"doc",get:function(){return Object(u["a"])(this._contextElement)}},{key:"win",get:function(){return Object(y["a"])(this._contextElement)}},{key:"activeElement",get:function(){return Object(O["a"])(this.doc)}},{key:"defaultFocusElement",get:function(){var e=this._options.defaultFocusElement
var t=Object(m["a"])("function"===typeof e?e():e)
if(t&&this._contextElement&&this._contextElement.contains(t))return t
var n=this.firstTabbable
if(n)return n
if(this.focusable.includes(this._contextElement))return this._contextElement
return null}}])
return e}()
var g=function(){function e(t,n){var i=this
Object(o["a"])(this,e)
this._contextElement=null
this._preventCloseOnDocumentClick=false
this._listeners=[]
this._active=false
this.handleDismiss=function(e,t){i._options.onDismiss(e,t)}
this.captureDocumentClick=function(e){var t=e.target
i._preventCloseOnDocumentClick=0!==e.button||Object(s["a"])(i._contextElement,t)}
this.handleDocumentClick=function(e){i._options.shouldCloseOnDocumentClick&&!i._preventCloseOnDocumentClick&&i.handleDismiss(e,true)}
this.handleFrameClick=function(e,t){Object(s["a"])(i._contextElement,t)||i.handleDismiss(e,true)}
this.handleKeyUp=function(e){i._options.shouldCloseOnEscape&&e.keyCode===a.a.codes.escape&&!e.defaultPrevented&&i.handleDismiss(e)}
this._options=n||{shouldCloseOnDocumentClick:true,shouldCloseOnEscape:true,onDismiss:function(e){}}
this._contextElement=t
this._screenReaderFocusRegion=new d(t,n)
this._keyboardFocusRegion=new N(t,n)
this._id=Object(h["a"])()}Object(i["a"])(e,[{key:"updateElement",value:function(e){this._contextElement=e
this._keyboardFocusRegion&&this._keyboardFocusRegion.updateElement(e)
this._screenReaderFocusRegion&&this._screenReaderFocusRegion.updateElement(e)}},{key:"activate",value:function(){var e=this
if(!this._active){var t=Object(u["a"])(this._contextElement)
this._keyboardFocusRegion.activate()
this._screenReaderFocusRegion.activate()
if(this._options.shouldCloseOnDocumentClick){this._listeners.push(Object(c["a"])(t,"click",this.captureDocumentClick,true))
this._listeners.push(Object(c["a"])(t,"click",this.handleDocumentClick))
Array.from(t.getElementsByTagName("iframe")).forEach((function(t){var n=l(t)
n&&e._listeners.push(Object(c["a"])(n,"mouseup",(function(n){e.handleFrameClick(n,t)})))}))}this._options.shouldCloseOnEscape&&this._listeners.push(Object(c["a"])(t,"keyup",this.handleKeyUp))
this._active=true}}},{key:"deactivate",value:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=e.keyboard,n=void 0===t||t
if(this._active){this._listeners.forEach((function(e){e.remove()}))
this._listeners=[]
n&&this._keyboardFocusRegion.deactivate()
this._screenReaderFocusRegion.deactivate()
this._active=false}}},{key:"focus",value:function(){this._active
this._keyboardFocusRegion.focus()}},{key:"blur",value:function(){this._active
this._keyboardFocusRegion.blur()}},{key:"id",get:function(){return this._id}},{key:"focused",get:function(){return this._active}},{key:"keyboardFocusable",get:function(){return(Object(f["a"])(this._contextElement)||[]).length>0}}])
return e}()},no2R:function(e,t,n){"use strict"
n.d(t,"a",(function(){return i}))
var o=n("kR0I")
function i(e,t){return Object(o["a"])(e,(function(e){return!r(e.getAttribute("tabindex"))}),t)}function r(e){return!isNaN(e)&&e<0}},yfCu:function(e,t,n){"use strict"
n.d(t,"a",(function(){return i}))
var o=n("QF4Q")
function i(e,t,n,i){var r=e===window||e===document?e:Object(o["a"])(e)
r.addEventListener(t,n,i)
return{remove:function(){r.removeEventListener(t,n,i)}}}}}])

//# sourceMappingURL=6-c-74bb245ec7.js.map