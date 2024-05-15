from libra import createPost, decorateMeta, decorateClassify

post = createPost("It Joke", "Erros r in line 21 when code has 20 lines!")

post_wirh_meta = decorateMeta(post, "Jhon Doe", "2024:01:01")

post_with_clas = decorateClassify(post, "History", list(("Old", "New")))
print(post_with_clas)
