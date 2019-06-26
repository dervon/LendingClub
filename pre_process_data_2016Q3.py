# copy from https://blog.csdn.net/a857553315/article/details/79394655
import pandas as pd
loans_2016S3 = pd.read_csv('LoanStats_2016Q3.csv', skiprows=1)
print(loans_2016S3.shape)
# 保留至少三分之一不为空的特征属性
half_count = len(loans_2016S3) * 2 / 3
# 保留多于thresh不为空的列属性
loans_2016S3 = loans_2016S3.dropna(thresh=half_count, axis=1)
print(loans_2016S3.shape)
# 删除desc属性，贷款原因的大段描述
#loans_2016S3 = loans_2016S3.drop(['desc'],axis=1)
loans_2016S3.to_csv('loans_2016S3.csv', index=False)
loans_2016S3 = pd.read_csv("loans_2016S3.csv")
# 删除特征
loans_2016S3 = loans_2016S3.drop([ "funded_amnt", "funded_amnt_inv", "grade", "sub_grade", "emp_title", "issue_d"], axis=1)
# 删除特征
loans_2016S3 = loans_2016S3.drop(["zip_code", "out_prncp", "out_prncp_inv", "total_pymnt", "total_pymnt_inv", "total_rec_prncp"], axis=1)
# 删除特征
loans_2016S3 = loans_2016S3.drop(["total_rec_int", "total_rec_late_fee", "recoveries", "collection_recovery_fee", "last_pymnt_d", "last_pymnt_amnt"], axis=1)
print(loans_2016S3.shape)
print(loans_2016S3.info())
# 打印贷款的申请结果类型及数量统计
print(loans_2016S3['loan_status'].value_counts())
# 只保留贷款成功和而不成功的情况，删除需要等待的情况
loans_2016S3 = loans_2016S3[(loans_2016S3['loan_status'] == "Fully Paid") | (loans_2016S3['loan_status'] == "Charged Off")]
status_replace = {
    "loan_status" : { "Fully Paid": 1,
                      "Charged Off": 0, }
}
# 将成功申请的情况用1代替，将申请失败的情况使用0代替
loans_2016S3 = loans_2016S3.replace(status_replace)
print(loans_2016S3.shape)
# 删除属性值只有一项的属性，因为其对预测没有任何意义
 
orig_columns = loans_2016S3.columns
drop_columns = []
for col in orig_columns:
    # 判断删除空值后是否是单一值
    col_series = loans_2016S3[col].dropna().unique()
    if len(col_series) == 1:
        drop_columns.append(col)
# 删除属性值单一的特征
loans_2016S3 = loans_2016S3.drop(drop_columns, axis=1)
# 打印单一的属性特征
print(drop_columns)
# 打印删除单一特征后剩下的特征属性数量
print(loans_2016S3.shape)
loans = loans_2016S3
null_counts = loans.isnull().sum() # 统计每列空值的个数
print(null_counts)
loans = loans.drop("pub_rec_bankruptcies", axis=1) # 空值多的，删除整列
loans = loans.dropna(axis=0) # 空值少的，直接删除该行
# 统计所有特征值的类型，并统计类型个数
print(loans.dtypes.value_counts()) # 统计特征类型的个数
# 寻找特征值是object类型特征，打印其第一个特征值
object_columns_df = loans.select_dtypes(include=["object"]) 
print(object_columns_df.iloc[0])
# 首先处理特征值中带有数值类型的特征
# 删除冗余的列
loans = loans.drop(["last_credit_pull_d", "earliest_cr_line", "addr_state", "title"], axis=1)
# 删除百分号
loans["int_rate"] = loans["int_rate"].str.rstrip("%").astype("float")
# 删除百分号
loans["revol_util"] = loans["revol_util"].str.rstrip("%").astype("float")
# 替换
mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}
loans = loans.replace(mapping_dict)
# 对于时间将最后的month去掉。只保留前面的月数
loans['term'] = loans['term'].apply(lambda x: int(x[:-7]))
object_columns_df = loans.select_dtypes(include=["object"]) 
# 寻找特征值是object类型特征的第一个特征值
print(object_columns_df.iloc[0])
cols = ['home_ownership', 'verification_status', "purpose", "debt_settlement_flag"]
for c in cols:
    print(loans[c].value_counts())# 打印每个object类型特征的特征值及个数
    print("================================")
# 对某列具有某几个不同的字符串类型的属性进行处理，进行get_dummies编码
cat_columns = ["home_ownership", "verification_status", "purpose", "debt_settlement_flag"]
dummy_df = pd.get_dummies(loans[cat_columns])
loans = pd.concat([loans, dummy_df], axis=1)
loans = loans.drop(cat_columns, axis=1)
# 查看最终的数据处理结果 
print(loans.info())
print(loans.shape)
loans[0:20]
#分离特征和标签
cols = loans.columns
train_cols = cols.drop("loan_status")
#标签
target = loans["loan_status"]
#特征值
features = loans[train_cols]
# 标准化
features = (features - features.mean(axis=0)) / (features.std(axis=0))
 
features["loan_status"] = target
print(features.shape)
features.to_csv('dealed_loans_2016S3--7.csv', index=False)
