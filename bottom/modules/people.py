from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivymd.uix.list import MDList, TwoLineAvatarIconListItem, ImageLeftWidget

people_list = [{"name": "Karel Nový", "state": "CZE"},
                {"name": "Karel Nový", "state": "CZE"},
                {"name":"Ivan Hrozný", "state":"RUS"},
                {"name": "John Walker", "state": "USA"}]

class MyItem(TwoLineAvatarIconListItem):
    def __init__(self, name, state, *args, **kwargs):
        super(MyItem, self).__init__(*args)
        self.text = name
        self.secondary_text = state
        self._no_ripple_effect = True
        self.image = ImageLeftWidget(source=f"images/{state}.png")
        self.add_widget(self.image)

class People(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(People, self).__init__(orientation="horizontal")
        scrollview = ScrollView()
        list = MDList()
        for person in people_list:
            list.add_widget(MyItem(name=person['name'], state=person['state']))
        scrollview.add_widget(list)
        self.add_widget(scrollview)
        
        