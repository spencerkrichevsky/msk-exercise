from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=[API Key])

# Read the reference report
ref = open('./data/cleaned_reports/cleaned_msk_sample_report.txt', 'r', encoding='utf-8').read()

# Set the prompt
prompt = 'Generate a comprehensive bone marrow report that recapitulates the type of report generated by an expert hematopathologist during the manual evaluation of a bone marrow biopsy acquired from a patient with a hematologic malignancy such as aplastic anemia, Hodgkin lymphoma, non-Hodgkin lymphoma, chronic myeloid leukemia, essential thrombocytosis, myelofibrosis, polycythemia vera, chronic myelomonocytic leukemia, myelodysplastic syndrome, acute myeloid leukemia, acute promyelocytic leukemia, B-cell acute lymphoblastic leukemia, T-cell acute lymphoblastic leukemia, chronic lymphocytic leukemia, follicular lymphoma, diffuse large B-cell lymphoma, plasma cell myeloma, or multiple myeloma. Use the following sample report as a reference: '

# Set output path
output_dir = './data/synthesized_reports/gpt/raw_reports'
if not os.path.exists(output_dir):
  os.makedirs(output_dir)

# Generate 50 synthesized reports
for i in range(50):
  response = client.chat.completions.create(model="gpt-4o", messages=[{'role': 'user', 'content': prompt+ref}])
  report = response.choices[0].message.content
  output_path = os.path.join(output_dir + f'report_{i}.txt')
  f = open(output_path, 'w', encoding='utf-8')
  f.write(report)
  f.close()
  print(f'Saved: {output_path}')

