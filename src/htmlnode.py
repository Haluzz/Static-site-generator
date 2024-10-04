class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_attributes = []
        for key, value in self.props.items():
            html_attributes.append(f"{key}='{value}'")
        return " ".join(html_attributes)
    
    def __repr__(self):
        props_str = self.props_to_html()
        
        children_tags = [child.tag for child in self.children]
        
        return (f"HTMLNode(tag='{self.tag}', "
                f"value='{self.value}', "
                f"children={children_tags}, "
                f"props='{props_str}')")
        