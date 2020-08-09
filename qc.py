import db
import pandas as pd


def map():
    query = ''' 
        select 
            vt.id,
            vt.date,
            vt.cost,
            vt.imei,
            vt.phone,
            vt.sales_type,
            ct.trans_id,
            ct.coustmer_id,
            ct.store,
            ct.trans_type,
            ct.state
        from vendor_transactions vt
        join vendor_sales_types vst
        on vt.sales_type= vst.code
        join company_transcation ct
        on vt.imei = ct.imei and vt.phone = ct.phone
        where vst.sales_type = 'Device'
    '''
    df = pd.read_sql(query,con=db.engine)
    print(df)
    df.to_sql('mappings',db.engine,if_exists = 'replace',index=False)
    
    query_imei = ''' 
        select 
            vt.id,
            vt.date,
            vt.cost,
            vt.imei,
            vt.phone,
            vt.sales_type,
            ct.trans_id,
            ct.coustmer_id,
            ct.store,
            ct.state,
            ct.trans_type
        from vendor_transactions vt
        join vendor_sales_types vst
        on vt.sales_type= vst.code
        join company_transcation ct
        on vt.imei = ct.imei
        where vst.sales_type = 'Device'
             
    '''
    df_imei = pd.read_sql(query_imei,con=db.engine)
    df_imei = df_imei[~df_imei['imei'].isin(df['imei'])]
    print(df_imei)
    df_imei.to_sql('mappings',db.engine,if_exists = 'append',index=False)

    query_phone = ''' 
        select 
            vt.id,
            vt.date,
            vt.cost,
            vt.imei,
            vt.phone,
            vt.sales_type,
            ct.trans_id,
            ct.coustmer_id,
            ct.store,
            ct.trans_type,
            ct.state
        from vendor_transactions vt
        join vendor_sales_types vst
        on vt.sales_type= vst.code
        join company_transcation ct
        on vt.phone = ct.phone
        where vst.sales_type = 'Device'
             
    '''
    df_phone = pd.read_sql(query_phone,con=db.engine)
    df_phone = df_phone[~df_phone['phone'].isin(df['phone'])]
    df_phone.to_sql('mappings',db.engine,if_exists = 'append',index=False)

if __name__ == "__main__":
    map()