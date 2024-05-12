from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

association_table = Table('association', Base.metadata,
                          Column('post_id', Integer, ForeignKey('posts.id')),
                          Column('tag_id', Integer, ForeignKey('tags.id'))
                          )


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    posts = relationship('Post', back_populates='author')


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    posts = relationship('Post', secondary=association_table, back_populates='tags')


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    posts = relationship('Post', back_populates='category')


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))

    author = relationship('Author', back_populates='posts')
    category = relationship('Category', back_populates='posts')
    tags = relationship('Tag', secondary=association_table, back_populates='posts')
   