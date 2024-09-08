init python:
    class Item():
        def __init__(self) -> None:
            self.inventory = set()
            self.found = set()
            self.used = set()

        def find(self, item: str) -> None:
            self.inventory.add(item)
            self.found.add(item)
            renpy.restart_interaction()

        def use(self, item: str) -> None:
            self.inventory.remove(item)
            self.used.add(item)
            renpy.restart_interaction()

        def is_inventory(self, item: str) -> bool:
            return item in self.inventory

        def is_found(self, item: str) -> bool:
            return item in self.found

        def is_used(self, item: str) -> bool:
            return item in self.used
