import csv
import json

def handle_duplicates(file_path, file_type, key_field=None, output_file_path=None):
  """
  Handles duplicate values in a text, CSV, or JSON file.

  Args:
    file_path: Path to the file.
    file_type: Type of the file ('text', 'csv', 'json').
    key_field: (Optional) For CSV and JSON, the field to use for identifying duplicates.
              If None, the entire line/row is considered for duplicates.

  Returns:
    A list of unique values (for text files) or a list of unique dictionaries/rows (for CSV and JSON).
  """

  unique_data = []
  seen = set()

  if file_type == 'text':
    with open(file_path, 'r') as f:
      for line in f:
        line = line.strip()  # Remove leading/trailing whitespace
        if line not in seen:
          unique_data.append(line)
          seen.add(line)

  elif file_type == 'csv':
    with open(file_path, 'r') as f:
      reader = csv.DictReader(f)
      for row in reader:
        if key_field:
          key = row[key_field]
        else:
          key = tuple(row.values())  # Use tuple for hashability
        if key not in seen:
          unique_data.append(row)
          seen.add(key)

  elif file_type == 'json':
    with open(file_path, 'r') as f:
      data = json.load(f)
      if isinstance(data, list):
        for item in data:
          if key_field:
            key = item[key_field]
          else:
            key = tuple(item.values())
          if key not in seen:
            unique_data.append(item)
            seen.add(key)
      elif isinstance(data, dict):
        unique_data = list(set(data.values()))

  if output_file_path:
    with open(output_file_path, 'w') as output_file:
      if file_type == 'text':
        output_file.write('\n'.join(unique_data))
      elif file_type == 'csv':
        fieldnames = unique_data[0].keys()  # Get fieldnames from the first row
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(unique_data)
      elif file_type == 'json':
        json.dump(unique_data, output_file, indent=2)
  return unique_data

# Example usage:
# Text file
unique_lines = handle_duplicates(r'D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\textduplicate.txt', 'text', output_file_path = r'D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\textduplicate_output.txt')

# CSV file (remove duplicates based on 'id' field)
unique_rows = handle_duplicates(r'D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\csvduplicate.csv', 'csv', key_field=None, output_file_path=r'D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\csvduplicate_output.csv')

# list JSON file (remove duplicates based on the 'name' field)
unique_items = handle_duplicates(r'D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\json-list-duplicate.json', 'json', key_field='name', output_file_path=r'D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\json-list-duplicate_output.json')

# dict JSON file (remove duplicates based on the 'name' field)
unique_items = handle_duplicates(r'D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\json-dict-duplicate.json', 'json', key_field='name', output_file_path=r'D:\JOB Mission 2024-25\BigData Engineer\Level-1-Mock\MockInterviewProgram\json-dict-duplicate_output.json')
