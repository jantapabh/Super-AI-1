import pandas as pd
import matplotlib.pyplot as plt
csv_file='covid_19_data.csv ' #เลือกข้อมูลของโรคระบาด Covid-19 ซึ่งข้อมูลในแต่ละแถวนั้นก็จะรายงานจำนวนผู้ติดเชื้อสะสม จำนวนผู้เสียชีวิต และผู้ป่วยที่หายแล้วแบบอัพเดทในแต่ละวัน
data = pd.read_csv(csv_file)
print(data)

