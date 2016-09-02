#coding=utf-8
from django.db import models 
# Create your models here.


# 机器人出厂音色编号集合
class ProductVocal(models.Model):
	voice_index = models.IntegerField(verbose_name=u'科大讯飞语音编号',default=0) #  科大讯飞语音编号
	class Meta:
		verbose_name = '机器人出厂音色编号'
		verbose_name_plural  = '机器人出厂音色编号'

# 机器人出厂唤醒词集合
class ProductWakeWord(models.Model):
	wake_up_word_index = models.IntegerField(verbose_name=u'科大讯飞唤醒词编号',default=0) # 科大讯飞唤醒词编号（出厂）
	class Meta:
		verbose_name = '科大讯飞唤醒词编号'
		verbose_name_plural  = '科大讯飞唤醒词编号'

# 家庭
class Falimy(models.Model):
	mobile = models.CharField(verbose_name=u'家庭电话',max_length=255,default="")
	android_id = models.CharField(verbose_name=u'安卓ID',max_length=255,default="")
	class Meta:
		verbose_name = "家庭"
		verbose_name_plural = "家庭"	

# 成员
class Member(models.Model):
	belonged_falimy = models.ForeignKey(Falimy,verbose_name=u'家庭',related_name='member_falimy')
	age = models.IntegerField(verbose_name=u'年龄',default=0) 
	sex = models.IntegerField(verbose_name=u'性别',default=0) # 0-男 1-女
	mobile = models.CharField(verbose_name=u'手机',max_length=255,blank=True,null=True)
	member_type = models.IntegerField(verbose_name=u'成员类别',default=0) # 0-成人 1-儿童

# 成员音色
class SpecifyVocal(models.Model):
	belonged_falimy = models.ForeignKey(Falimy,verbose_name=u'家庭',related_name='voice_falimy')
	specify_voice_index = models.IntegerField(verbose_name=u'科大讯飞语音编号',default=0) #  科大讯飞语音编号

	class Meta:
		verbose_name = "家庭发音音色"
		verbose_name_plural = "家庭发音音色"

# 唤醒词 or 特定声音
class WakeupWord(models.Model):
	word = models.CharField(verbose_name=u'唤醒词语',max_length=255,default="")
	specify_voice = models.ForeignKey(SpecifyVocal,verbose_name=u'唤醒声音')
	class Meta:
		verbose_name = '唤醒词'
		verbose_name_plural  = '唤醒词'

# 成员人脸数据
class MemberFace(models.Model):
	belonged_member = models.ForeignKey(Member,verbose_name=u'所属成员',related_name='member_face')
	face_img_link = models.CharField(verbose_name=u'人脸图片链接地址',max_length=255,default="")
	predict_age = models.IntegerField(verbose_name=u'预测年龄',default=0)

# 成员声纹数据
class MemberVocalPrint(models.Model):
	belonged_member = models.ForeignKey(Member,verbose_name=u'所属成员',related_name='member_vocal_print')
	vocal_print_link = models.CharField(verbose_name=u'声纹数据链接地址',max_length=255,default="")



