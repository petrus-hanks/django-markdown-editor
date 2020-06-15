# -*- coding: utf-8 -*-
# @Author: runzhangHan
# @Date:   2020-06-15 13:18:19
# @Last Modified by:   runzhangHan
# @Last Modified time: 2020-06-15 13:22:19
from django.test import TestCase
from app.models import Post

class PostTestCase(TestCase):
	def testPost(self):
		post = Post(title="My Title", description="Blurb", wiki="Post Body")
		self.assertEqual(post.title, "My Title")
		self.assertEqual(post.description, "Blurb")
		self.assertEqual(post.wiki, "Post Body")
		