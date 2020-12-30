from django.db import models

# Create your models here.
class Todo(models.Model):  # 필드와 그 옵션을 정의합니다.
    title = models.CharField(
        max_length=64,
        verbose_name="제목",
        help_text="제목"
    )
    description = models.CharField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name="설명",
        help_text="설명"
    )
    author = models.CharField(
        max_length=16,
        verbose_name="작성자",
        help_text="작성자"
    )
    due_date = models.DateTimeField(
        verbose_name="마감일",
        help_text="마감일"
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="완료 여부",
        help_text="완료 여부"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
        verbose_name="생성 일시",
        help_text="데이터가 생성된 날짜 시간"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        blank=True,
        null=False,
        verbose_name="수정 일시",
        help_text="데이터가 수정된 날짜 시간"
    )


    # verbose_name: 모델 객체의 이름으로 관리자 화면 등에서 표시됩니다.
    # verbose_name_plural: 영어를 기준으로 복수형입니다. 옵션을 지정하지 않으면 verbose_name에 s를 붙입니다.
    # ordering: '-created' 라는 필드를 기준으로 내림차순으로 정렬합니다.
    class Meta:
        verbose_name = '할일 목록'
        verbose_name_plural = '핧일 목록'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Todo {self.title}/{self.author}/{self.created_at}"