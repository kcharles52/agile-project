import datetime

class Comment(object):

    comments_list = []

    def __init__(self, message, author):
        self.message = message
        self.author = author
        self.timestamp = datetime.datetime.utcnow()

    # add comment method
    def add_comment(self):
        Comment.comments_list.append(self)
        print('comment successfully added')

    # edit comment method
    def edit_comment(self):
        print('comment successfully modified')

    # delete comment method
    def delete_comment(self):
        print('comment successfully deleted')
        

    