class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return None
        html_props = ""

        for prop in self.props:
            html_props += f' {prop}="{self.props[prop]}"'
        return html_props

    def __repr__(self):
        return f"tag:{self.tag}, value:{self.value}, children:{self.children}, props:{self.props}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError()
        elif not self.tag:
            return self.tag
        else:
            if self.props:
                return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"tag:{self.tag}, value:{self.value}, props:{self.props}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("no tag")
        if self.children is None:
            raise ValueError("no children")

        return_html = ""
        for node in self.children:
            return_html += node.to_html()
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{return_html}</{self.tag}>"
        else:
            return f"<{self.tag}>{return_html}</{self.tag}>"

    def __repr__(self):
        return f"tag:{self.tag}, children:{self.children}, props:{self.props}"
