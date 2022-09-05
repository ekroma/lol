# 1

# class Smartphone:
#     def call(self):
#         print('вы звоните на какой то номер')
    
#     def where_to_wear(self):
#         print('You can keep me anywhere')
 
# class Watch:
#     def see_time(self):
#         import time
#         a = time.localtime()
#         current_time = time.strftime("%H:%M:%S", a)
#         print(current_time)
    
#     def where_to_wear(self):
#         print('You should wear me on your hand')

# class Smartwatch(Smartphone, Watch):
#     def where_to_wear(self):
#         return Watch().where_to_wear()

# sm = Smartwatch()
# sm.call()
# sm.see_time()
# sm.where_to_wear()


# 2

# class Log_Pass_Mixin:
#     def post(self, username, password):
#         if username == self.username and password == self.password:
#             print('Successfully created')
#         else:
#             print('Wront username or password')

# class Instagram(Log_Pass_Mixin):
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def post_post(self, post, username, password):
#         super().post(username, password)

# class TikTok(Log_Pass_Mixin):
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password 

#     def post_video(self, post, username, password):
#         return super().post(username, password)

# inst = Instagram('kopik', 1234)
# tik = TikTok('tolik', 4321)

# inst.post_post('birthday', 'kopik', 1234)
# tik.post_video('birthday', 'tolik', 4321)