"""
WARNING:

Please make sure you install the bot dependencies with `pip install --upgrade -r requirements.txt`
in order to get all the dependencies on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the dependencies.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install --upgrade -r requirements.txt`
- Use the same interpreter as the one used to install the bot (`pip install --upgrade -r requirements.txt`)

Please refer to the documentation for more information at
https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# Import for the Desktop Bot
from botcity.core import DesktopBot, Backend

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    ## Fetch the BotExecution with details from the task, including parameters
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = DesktopBot()

    # Implement here your logic...
    app_path = r"C:\Users\diego\Documents\Estudos\PYTHON\Projetos em BotCity\MyCRM\MyCRM.exe"
    #bot.execute(app_path)

    # Conectando -se ao aplicativo usando os seletores de 'path' e 'title'.
    app = bot.connect_to_app(Backend.UIA, path = app_path, title="My CRM (Sample App)")

    # Procurando o elemento que está no contexto da janela encontrada.
    first_field = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "textBoxPeopleFirstName")
    #Inserindo o texto
    first_field.set_text("Diego")

    last_field = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "textBoxPeopleLastName")
    last_field.set_text("Henrique")

    comments_field = bot.find_app_element(from_parent_window = app.top_window(), auto_id = "textBoxPeopleComments")
    coment = "Testando o BotCity Desktop Automation na aula de Python RPA do Marcelo Cruz"
    comments_field.set_text(coment)

    # Uncomment to mark this task as finished on BotMaestro
    # maestro.finish_task(
    #     task_id=execution.task_id,
    #     status=AutomationTaskFinishStatus.SUCCESS,
    #     message="Task Finished OK."
    # )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()