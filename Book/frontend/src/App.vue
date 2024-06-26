<template>
    <el-container class="container">
      <el-header class="el-header">
        <h2>书籍生成系统</h2>
          <el-select style="width: 250px" v-model="value" placeholder="请选择书籍类型" size="large">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value"
            />
          </el-select>
      </el-header>
      <novel v-if="value===1"/>
      <biography v-else-if="value===2"/>
      <history v-else-if="value===3"/>
      <encyclopedia v-else-if="value===4"/>
      <textbook v-else-if="value===5"/>
      <method v-else-if="value===6"/>
      <customize v-else-if="value===7"/>
    </el-container>
</template>

<script>
import novel from './components/novel.vue';
import biography from './components/biography.vue';
import encyclopedia from './components/encyclopedia.vue';
import history from './components/history.vue';
import textbook from './components/textbook.vue';
import method from './components/method.vue';
import customize from './components/customize.vue';

export default {
  data() {
    return{
      value : 1,
      options:[
        {
          value: 1,
          label: '小说',
        },
        {
          value: 2,
          label: '传记',
        },
        {
          value: 3,
          label: '历史书',
        },
        {
          value: 4,
          label: '百科书',
        },
        {
          value: 5,
          label: '教科书',
        },
        {
          value: 6,
          label: '方法论',
        },
        {
          value: 7,
          label: '自定义',
        },
      ],
      colorBlockTop: 0,
      colorBlockLeft: 0,
    }
  },
  components: {
    novel,
    biography,
    encyclopedia,
    history,
    textbook,
    method,
    customize,
  }
};
</script>

<style>
.container {
  background-color: rgba(173, 173, 173, 0.2);
  height: 100vh;
  display: flex;
  flex-direction: column;
  position: relative;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3); /* 添加阴影效果 */
  border-radius: 10px;
}
.el-header {
  background-color: rgb(0, 0, 0, 0.8);
  height: 9vh;
  padding: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: #fff;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.8); /* 添加阴影效果 */
  border-radius: 5px;
}
.el-aside {
  background-color: rgb(194, 194, 194, 0.3);
  height: 91vh;
  padding: 20px;
  display: flex;
  justify-content: center;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.3); /* 添加阴影效果 */
  border-radius: 10px;
}
.el-main {
  height: 91vh;
  padding: 20px;
}
</style>