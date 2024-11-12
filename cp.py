import os
import csv
import json
import shutil

uids = [
    'd405ceed-68da-4e50-a0ef-5d2995a94e5d_QA-139',
    '16a54f9d-6729-442a-8d39-3e7db4215f57_QA-19',
    'd9db7166-e5fe-4ce5-85eb-0c437c4ddf32_QA-19',
    '8f9f4689-cf3e-4a69-88b0-81ea3a9f5805_QA-2',
    'ca6e9ec9-46ac-4a02-8034-7c31157dc52c_QA-2',
    '56200f81-8dd1-4423-9b97-cf5c2e545efa_QA-1',
    '275ea957-7404-4e86-ae6c-e3e1cb988b37_QA-17',
    'e9e0f26d-3005-436a-a70f-7d99977808c8_QA-3',
    'f71fb12c-211c-495b-a893-1f73e0538475_QA-0',
    'ec9fd60f-578b-4e29-b016-b6a424b064f4_QA-3',
    '806cc2eb-1c00-400f-a302-7b54541de381_QA-6',
    '8672b38a-7682-4244-ad7a-a336c81c2d0e_QA-19',
    'c847fafa-725f-4e25-843e-84e4cca97ce0_QA-36',
    '5fce50cf-ebc5-4c09-8704-20c48fe42c7e_QA-72',
    '84a442a4-6271-40ee-a524-2244786f662e_QA-13',
    '4cb9441e-06eb-4f82-8acf-0cc09be8b8df_QA-9',
    '11b71158-ee80-448c-b02b-2d2b3efc5d17_QA-53',
    'bf591b19-c972-4adf-ab56-aa57b149c3ca_QA-246',
    '2db7efae-7b79-45f8-a35f-ab903958a9a9_QA-0',
    'de130a10-2c84-4006-b112-d90c8860804f_QA-52',
    'd1d1b6da-e7f8-48e7-9ee4-d8382582695a_QA-19',
    '0dedbbb0-d1a4-4231-a980-2b43acc08cb2_QA-62',
    '5dcbcc43-6220-457a-8e79-36ef9997eb90_QA-0',
    '17be1d0a-f213-4126-ab6e-08e5c8ee5b93_QA-30'
]

# for uid in uids:
#     shutil.copy(
#         f'/group/40007/luqiu/Ego4D_benchmark_pipeline/output_clip_total_6000/{uid}.mp4',
#         f'/group/40007/luqiu/Ego4D_benchmark_release/egoplanbench2/static/Videos/{uid}.mp4'
#     )

# videos = os.listdir('/group/40007/luqiu/Ego4D_benchmark_release/egoplanbench2/static/Videos')
# print(len(videos))

result_csv = '/group/40007/luqiu/Ego4D_benchmark_release/egoplanbench2/static/Videos/examples.csv'
with open(result_csv, 'a') as f:
    writer = csv.writer(f)
    writer.writerow(['select', 'question', 'options', 'label', 'video_path'])

datasets = json.load(open('/group/40007/luqiu/Ego4D_benchmark_release/EgoPlan-Bench2/EgoPlan-Bench2.json'))
rows = []
for uid in uids:
    for dataset in datasets:
        if dataset['sample_id'].split('_') == uid.split('_QA-'):
            rows.append([
                f"{dataset['domain']} - {dataset['scenario']}",
                f"Considering the progress shown in the video and my current observation in the last frame, what action should I take next in order to {dataset['task_goal']}?",
                f"A. {dataset['choice_a']}, B. {dataset['choice_b']}, C. {dataset['choice_c']}, D. {dataset['choice_d']}",
                f"{dataset['golden_choice_idx']}. {dataset['answer']}",
                f"./static/Videos/{uid}.mp4"
            ])
            break

rows.sort()
for row in rows:
    with open(result_csv, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)

