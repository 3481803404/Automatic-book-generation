<template>
  <el-container>
    <el-aside class="el-aside">
      <transition name="slide">
      <el-form
          ref="form"
          :model="form"
          :rules="rules"
          style="max-width: 600px"
          label-width="auto">
        <el-form-item label="国家或地区" prop="country">
          <el-input v-model="form.country" placeholder="请输入国家或地区"></el-input>
        </el-form-item>

        <el-form-item label="时间段" prop="timePeriod">
          <el-input v-model="form.timePeriod" placeholder="请输入时间段"></el-input>
        </el-form-item>

        <el-form-item label="侧重点" prop="focusPoints">
          <el-checkbox-group v-model="form.focusPoints">
            <el-checkbox label="科技"></el-checkbox>
            <el-checkbox label="宗教"></el-checkbox>
            <el-checkbox label="社会"></el-checkbox>
            <el-checkbox label="文化"></el-checkbox>
            <el-checkbox label="经济"></el-checkbox>
            <el-checkbox label="军事"></el-checkbox>
            <el-checkbox label="重要历史事件"></el-checkbox>
          </el-checkbox-group>
        </el-form-item>

        <el-form-item label="书籍章节数" prop="chapterCount">
          {{form.chapterCount}}
          <el-slider v-model="form.chapterCount" :min="1" :max="10"></el-slider>
        </el-form-item>

        <el-form-item label="书籍标题" prop="title">
          <el-input v-model="form.title" placeholder="请输入书籍标题"></el-input>
        </el-form-item>

        <el-form-item label="其他内容或要求" prop="other">
          <el-input v-model="form.other" placeholder="其他内容或要求"></el-input>
        </el-form-item>

        <el-form-item>
          <el-button type="primary" @click="submitForm('form')">提交</el-button>
          <el-button @click="resetForm('form')">重置</el-button>
        </el-form-item>
      </el-form>
      </transition>
    </el-aside>
    <transition name="fade">
      <el-main class="el-main" v-if="bookTitle!==''">
        <div v-if="currentPage === 1">
          <h1>{{ bookTitle }}</h1>
          <ul>
            <li v-for="(chapter, index) in chapters" :key="index">
              <a @click="goToChapter(index)">{{ chapter.title }}</a>
            </li>
          </ul>
          <el-button type="primary" @click="saveBook(currentPage-1)">保存为word文件</el-button>
        </div>
        <div v-else>
          <h1>{{ currentChapter.title }}</h1>
          <p>{{ currentChapter.content }}</p>
          <el-button type="primary" @click="renewChapter(currentPage-1)">重新生成本章内容</el-button>
        </div>
        <el-pagination
            v-if="totalPages > 1"
            @current-change="handlePageChange"
            :current-page="currentPage"
            :page-size="1"
            :total="totalPages"
            layout="prev, pager, next"
        />
      </el-main>
    </transition>
  </el-container>
</template>

<script>
import {post} from "../assets/post.js";
import { gsap } from 'gsap';

export default {
  data() {
    return {
      form: {
        key:3,
        country: '',
        timePeriod: '',
        focusPoints: [],
        chapterCount: 2,
        title: '',
        other: ''
      },
      rules: {
        country: [{ required: true, message: '请输入国家或地区', trigger: 'blur' }],
        timePeriod: [{ required: false, message: '请输入时间段', trigger: 'blur' }],
        focusPoints: [{ required: true, type: 'array', min: 1, message: '请选择侧重点', trigger: 'change' }],
        title: [{ required: false, message: '请输入书籍标题', trigger: 'blur' }],
      },
      bookTitle: '',
      chapters: '',
      currentPage: 1,
    };
  },
  computed: {
    totalPages() {
      return this.chapters.length + 1; // Plus one for the initial page
    },
    currentChapter() {
      if (this.currentPage === 1) {
        return null; // No chapter to display on the first page
      } else {
        return this.chapters[this.currentPage - 2]; // Minus two to adjust for zero-based indexing and initial page
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate(valid => {
        if (valid) {
          // 表单验证通过，执行提交操作
          console.log('提交成功');
          const url = 'http://127.0.0.1:5000/generate_book';
          const data = this.form;
          post(url, data)
              .then(data => {
                console.log('POST请求成功:', data);
                this.bookTitle=data.title;
                this.chapters=data.chapters;
                this.currentPage=1;
                // 处理返回的数据
              })
              .catch(error => {
                console.error('POST请求失败:', error);
                // 处理错误情况
              })
              .finally(() => {
                gsap.from('.el-main', {x: 100, opacity: 0, duration: 1});
              });
        } else {
          // 表单验证失败
          console.log('表单验证失败');
          return false;
        }
      });
    },
    resetForm(formName) {
      this.$refs[formName].resetFields();
      this.bookTitle='';
      this.chapters='';
    },
    goToChapter(index) {
      this.currentPage = index + 2;
      gsap.from('.el-main', { x: 100, opacity: 0, duration: 1 });
    },
    handlePageChange(page) {
      if(page>this.currentPage)
        gsap.from('.el-main', { x: 100, opacity: 0, duration: 1 });
      else gsap.from('.el-main', { x: -20, opacity: 0, duration: 0.4 });
      this.currentPage = page;
    },
    renewChapter(index){
      const url = 'http://127.0.0.1:5000/renew_chapter';
      const data = {'index':index,
        'chapter':this.chapters[index-1]};
      post(url, data)
          .then(data => {
            console.log('POST请求成功:', data);
            this.chapters[index-1]=data;
            this.currentPage=index+1;
            // 处理返回的数据
          })
          .catch(error => {
            console.error('POST请求失败:', error);
            // 处理错误情况
          })
          .finally(() => {
            gsap.from('.el-main', {y: 100, opacity: 0, duration: 1});
          })
    },
    saveBook(){
      const url = 'http://127.0.0.1:5000/save_book';
      const data = {'title':this.bookTitle,'chapters':this.chapters};
      const requestOptions = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
        mode:"cors"
      };
      fetch(url, requestOptions)
          .then(response => {
            // 将二进制数据转换为Blob对象
            return response.blob();
          })
          .then(blob => {
            // 创建一个临时的URL来访问Blob对象
            let url = window.URL.createObjectURL(blob);
            // 创建一个链接元素来下载文件
            let a = document.createElement('a');
            a.href = url;
            a.download = this.bookTitle+'.docx';
            // 模拟点击链接以触发下载
            a.click();
            // 释放对象URL
            window.URL.revokeObjectURL(url);
          })
          .catch(error => {
            console.error('Error downloading file: ', error);
          });
    },
  },
  mounted() {
    // 使用 gsap 定义动画效果
    gsap.from('.el-aside', { x: -100, opacity: 0, duration: 1 });
    gsap.from('.el-main', { x: 100, opacity: 0, duration: 1 });
  },
};
</script>
