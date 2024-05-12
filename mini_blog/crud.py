from sqlalchemy.orm import Session
import models
import schemas


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return {
        'id': db_author.id,
        'name': db_author.name
    }


def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def create_post(db: Session, post: schemas.PostCreate):
    tags = [db.query(models.Tag).get(tag_id) for tag_id in post.tags]
    db_post = models.Post(**post.dict(exclude={"tags"}))
    db_post.tags = tags
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
