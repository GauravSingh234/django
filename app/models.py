from django.db import models
# from django.test import TestCase
import logging


# Create your models here.

# logger = logging.getLogger(__name__)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publication_date = models.DateField()
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField(null=True)

    

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=45)
    biography = models.CharField(max_length=200)
    dob = models.DateField()

    def __str__(self):
        return self.name



class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=250)
    mobile = models.CharField(max_length=15)


    def __str__(self):
        return self.name




    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         logger.info(f"Book '{self.title}' (ID: {self.pk}) is being updated.")
    #     else:
    #         logger.info(f"A new book '{self.title}' is being created.")
    #     super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     logger.warning(f"Book '{self.title}' (ID: {self.pk}) is being deleted.")
    #     super().delete(*args, **kwargs)






    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         logger.info(f"Author '{self.name}' (ID: {self.pk}) is being updated.")
    #     else:
    #         logger.info(f"A new author '{self.name}' is being created.")
    #     super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     logger.warning(f"Author '{self.name}' (ID: {self.pk}) is being deleted.")
    #     super().delete(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         logger.info(f"Publisher '{self.name}' (ID: {self.pk}) is being updated.")
    #     else:
    #         logger.info(f"A new publisher '{self.name}' is being created.")
    #     super().save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     logger.warning(f"Publisher '{self.name}' (ID: {self.pk}) is being deleted.")
    #     super().delete(*args, **kwargs)




# class AuthorModelTest(TestCase):
#     def setUp(self):
#         self.author = Author.objects.create(name="J.K. Rowling", biography="Author of Harry Potter", dob="2024-08-13")
    
#     def test_author_creation(self):
#         """Test that an Author object is created correctly."""
#         self.assertEqual(self.author.name, "J.K. Rowling")
#         self.assertEqual(self.author.biography, "Author of Harry Potter")
#         self.assertEqual(self.author.dob, "2024-08-13")

#     def test_author_str_method(self):
#         """Test the string representation of the Author model."""
#         self.assertEqual(str(self.author), "J.K. Rowling")


# class PublisherModelTest(TestCase):
#     def setUp(self):
#         self.publisher = Publisher.objects.create(name="Bloomsbury", address="London", mobile="1234567890")
    
#     def test_publisher_creation(self):
#         """Test that a Publisher object is created correctly."""
#         self.assertEqual(self.publisher.name, "Bloomsbury")
#         self.assertEqual(self.publisher.address, "London")
#         self.assertEqual(self.publisher.mobile, "1234567890")

#     def test_publisher_str_method(self):
#         """Test the string representation of the Publisher model."""
#         self.assertEqual(str(self.publisher), "Bloomsbury")


# class BookModelTest(TestCase):
#     def setUp(self):
#         self.author = Author.objects.create(name="J.K. Rowling", biography="Author of Harry Potter", dob="1965-07-31")
#         self.publisher = Publisher.objects.create(name="Bloomsbury", address="London", mobile="1234567890")
#         self.book = Book.objects.create(
#             title="Harry Potter and the Philosopher's Stone",
#             author=self.author,
#             publication_date="1997-06-26",
#             publisher=self.publisher,
#             description="The first book in the Harry Potter series.",
#             price=19.99,
#             stock=100
#         )

#     def test_book_creation(self):
#         """Test that a Book object is created correctly."""
#         self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")
#         self.assertEqual(self.book.author.name, "J.K. Rowling")
#         self.assertEqual(self.book.publication_date, "2024-08-13")
#         self.assertEqual(self.book.publisher.name, "Bloomsbury")
#         self.assertEqual(self.book.description, "The first book in the Harry Potter series.")
#         self.assertEqual(self.book.price, 19.99)
#         self.assertEqual(self.book.stock, 100)

#     def test_book_str_method(self):
#         """Test the string representation of the Book model."""
#         self.assertEqual(str(self.book), "Harry Potter and the Philosopher's Stone")




