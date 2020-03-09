import facebook
import json
import pandas as pd

class GetData:
	def __init__(self):
		self.fbtoken = open("token.txt","r").read()
		self.fbpageId = open("pageid.txt","r").read()
		self.comments = pd.DataFrame(columns = ['postId','comments'])
		self.graph = facebook.GraphAPI(access_token=self.fbtoken, version="3.1")

	def fetch_facebook_data(self):
		
		self.posts = self.graph.get_object(id=self.fbpageId + '/feed', fields='message')
		# for post in self.posts['data']:
		# 	print (post['id'])

	def getComments(self):
		index = 0
		for post in self.posts['data']:
			comments = self.graph.get_object(id = post['id'] + '/comments', fields='message')
			print (str(post['id']))
			if len(comments['data']) != 0:
				self.comments.loc[index] = [str(post['id']), comments['data']['message']]
			else:
				self.comments.loc[index] = [str(post['id']), []]
			
		print (self.comments)



if __name__ == "__main__":
	data = GetData()
	data.fetch_facebook_data()
	data.getComments()