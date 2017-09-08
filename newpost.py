# A program to create the header of a new blog post for a Jekyll blog
import time

def main():
	file = input('File name: ')
	title = input('Title: ')
	desc = input('Description: ')
	pl = input('Permalink: /')

	filename = file + '.md'
	f = open(filename,"w+")

	f.write('---\n')
	f.write('layout: post\n')
	f.write('title: "{}"\n'.format(title))
	f.write('date: ' + time.strftime("%d-%m-%Y")+'\n')
	f.write('author: Chad Purdy\n')
	f.write('description: ' + desc + '\n')
	f.write('tags:\n')
	f.write('- blogs\n')
	f.write('categories:\n')
	f.write('- blogs\n')
	f.write('permalink: /'+pl + '\n')
	f.write('---')
	f.close()

main()