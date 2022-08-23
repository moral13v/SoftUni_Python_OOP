from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def __get_object_by_id(item_id, collection):
        for item in collection:
            if item.id == item_id:
                return item

    @staticmethod
    def __validate_and_add_object(obj, collection):
        if obj not in collection:
            return collection.append(obj)

    @staticmethod
    def __validate_and_delete_object(obj, collection):
        if obj in collection:
            return collection.remove(obj)

    def add_category(self, category: Category):
        self.__validate_and_add_object(category, self.categories)

    def add_topic(self, topic: Topic):
        self.__validate_and_add_object(topic, self.topics)

    def add_document(self, document: Document):
        self.__validate_and_add_object(document, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        category = self.__get_object_by_id(category_id, self.categories)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__get_object_by_id(topic_id, self.topics)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__get_object_by_id(document_id, self.documents)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__get_object_by_id(category_id, self.categories)
        self.__validate_and_delete_object(category, self.categories)

    def delete_topic(self, topic_id):
        topic = self.__get_object_by_id(topic_id, self.topics)
        self.__validate_and_delete_object(topic, self.topics)

    def delete_document(self, document_id):
        document = self.__get_object_by_id(document_id, self.documents)
        self.__validate_and_delete_object(document, self.documents)

    def get_document(self, document_id):
        document = self.__get_object_by_id(document_id, self.documents)
        return document

    def __repr__(self):
        return '\n'.join([repr(document) for document in self.documents])












