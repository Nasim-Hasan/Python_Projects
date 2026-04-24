import aisuite as ai
from dotenv import load_dotenv
_ = load_dotenv()
# Create an instance of the AISuite client
client = ai.Client()

# Write a text file
def write_txt_file(file_path: str, content: str)->str:
    """
    Write a string into a .txt file (overwrites if exists).
    Args:
    file_path (str): Destination path.
    content (str): Text to write.
    Returns:
    str: Path to the written file.
    """
    with open(file_path, "w", encoding="utf-8") as f:
     f.write(content)
    return file_path

prompt = "Can you make a txt note for me called reminders.txt that reminds me to call?" 
response = client.chat.completions.create(
model="openai:o4-mini",
messages=[{"role": "user", "content": (
prompt
)}],
tools=[write_txt_file],
max_turns=5
)
print(response)