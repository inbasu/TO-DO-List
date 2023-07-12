from dotenv import dotenv_values, find_dotenv

# load env
env = dotenv_values(find_dotenv())
# take vars
key = env["SECTER_KEY"]
