import command_system

def help(*args):
	message=""
	for c in command_system.command_list:
		message+=c.keys[0]+" - "+ c.description +"\n"
	return message

help_command=command_system.Command()

help_command.keys = ['!help']
help_command.description = "Помощь"
help_command.process = help