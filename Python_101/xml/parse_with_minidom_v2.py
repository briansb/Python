import xml.dom.minidom as minidom

def getTitles(xml):
    """
    Print out all titles found in xml
    """
    doc = minidom.parse(xml)
    node = doc.documentElement
    books = doc.getElementsByTagName("book")
    
    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        
        titles.append(titleObj)

    nodes = []
    for title in titles:
        nodesObj = title.childNodes
        nodes.append(nodesObj)
        print(nodes)

    print(len(nodes))
    for node in nodes:
        print(node.data)
        if node.nodeType == node.TEXT_NODE:
            print(node.data)

if __name__ == "__main__":
    document = 'example.xml'
    getTitles(document)    
