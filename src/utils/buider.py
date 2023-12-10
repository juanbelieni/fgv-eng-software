from kivy.uix.boxlayout import BoxLayout


class BoxLayoutBuilder(BoxLayout):

    def set_orientation(self, orientation):
        self.orientation = orientation
        return self

    def set_spacing(self, spacing):
        self.spacing = spacing
        return self

    def set_padding(self, padding):
        self.padding = padding
        return self

    def set_size(self, size):
        self.size = size
        return self

    def set_size_hint(self, size_hint):
        self.size_hint = size_hint
        return self

    def build(self): ...