import os.path


def write_file(tool, filename, content):
	file = open(os.path.join("logs", f'{tool}.{filename}'), 'w+')
	file.write(content)
	file.close()
  