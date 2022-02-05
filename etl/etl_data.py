import shelve
import pandas as pd
from project.models import Vulnerability
from datetime import datetime


class VulnerabilityETL:
    def extract(self):
        df = pd.read_csv(r'C:\Users\eduardonascimento\Documents\django\django_csv\data\asset_vulnerability.csv', sep=',')
        
        #print(df.head())
        return df

    def transform(self, df):
        pd.set_option("display.max_rows", 200, "display.max_columns", 200)

        df = pd.DataFrame(df)
        df = df.rename(columns={'ASSET - HOSTNAME': 'hostname', 
                                'ASSET - IP_ADDRESS': 'ip_address',
                                'VULNERABILITY - TITLE': 'title', 
                                'VULNERABILITY - SEVERITY': 'severity',
                                'VULNERABILITY - CVSS': 'cvss',
                                'VULNERABILITY - PUBLICATION_DATE': 'publication_date'})
        df = df.sort_values(by='hostname').reset_index(drop=True)
        return df

    def load(self, df):
        
        df_dict = df.to_dict()
        for index in range(0, len(df.index)):
            obj, created = Vulnerability.objects.update_or_create(
            hostname=df_dict['hostname'][index],
            ip_address=df_dict['ip_address'][index],
            title=df_dict['title'][index],
            severity=df_dict['severity'][index],
            cvss=df_dict['cvss'][index],
            publication_date=None if str(df_dict['publication_date'][index]) == 'nan' else datetime.strptime(str(df_dict['publication_date'][index]), '%Y-%m-%d'),
            )
        return created



vulnerability_etl = VulnerabilityETL()
df_vun = vulnerability_etl.load(vulnerability_etl.transform(vulnerability_etl.extract()))
df_vun1 = vulnerability_etl.transform(vulnerability_etl.extract())
