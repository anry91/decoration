def createPost(title,body):
    return{
        'title': title,
        'body': body,

    }
def decorateMeta(post, author, date):
    post['meta']= {
        'author': author,
        'date' : date,
    }
    return post
def decorateClassify(post, category, tags ):
    post['classify']={
        'category' : category,
        'tags': tags,
    }
    return post