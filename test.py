# -*- coding: utf-8 -*-
# @Time    : 2023/6/5 1:37
# @Author  : hjxylgogogo
# @File    : test.py.py
# @Software: PyCharm
from util import *
from qdrant_client import QdrantClient

collection_info = client.get_collection(collection_name="zhongyi_collection")
q ="【方剂名称】： 麻黄汤 【方剂出处】： 《伤寒论》 【方剂歌诀】： 麻黄汤中用桂枝，杏仁甘草四般施；发热恶寒头项痛，喘而无汗服之宜。 【方解】： 　　本方为治疗外感风寒表实证主要方剂。方中麻黄味苦辛性温，为肺经专药，能发越人体阳气，有发汗解表，宣肺平喘作用，所以是方中之君（主）药，并用之作为方名。由于营涩卫郁，单用麻黄发汗，但解卫气之郁，所以又用温经散寒，透营达卫之桂枝之臣（辅）药，加强发汗解表而散风寒，除身疼。本证喘是由肺气郁而上逆所致，麻、桂又都上行而散，所以再配以降肺气、散风寒之杏仁为佐药，同麻黄一宣一降，增强解郁平喘之功。炙甘草既能调和宣降之麻、桂，又能缓和麻、桂枝相合的峻烈之性，使汗出而不耗正气，是使药而兼佐药之义。诸药合用，共凑发汗解表，宣肺平喘之功。 【配方组成】： 麻黄9克、桂枝6克、杏仁9克、炙甘草3克。 【使用方法】： 　　水煎，分二次温服，微汗为度。 【功效和作用】： 　　外感风寒表实证。症见恶寒发热、头痛身痛、无汗而喘、苔薄白、脉浮紧。 【临床应用】： 　　本方常用于感冒、流行性感冒、急性支气管炎、支气管哮喘等属风寒表实证者。\n"
q_v = embedding(q)

hits = client.search(
    collection_name="zhongyi_collection",
    query_vector=q_v,
    limit=5  # Return 5 closest points
)
pass