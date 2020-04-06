import xml.dom.minidom

doc = xml.dom.minidom.parse("samplexml.xml")
print(doc.nodeName)
print(doc.firstChild.tagName)

# get a list of tag names
skills = doc.getElementsByTagName("skill")
print(skills.length)
for skill in skills:
    print(skill.getAttribute("name"))

new_skill = doc.createElement("skill")
new_skill.setAttribute("name", "jQuery")
doc.firstChild.appendChild(new_skill)

skills = doc.getElementsByTagName("skill")
print(skills.length)
for skill in skills:
    print(skill.getAttribute("name"))
