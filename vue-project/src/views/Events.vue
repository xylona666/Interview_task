<script>
import axios from 'axios';

export default {
  data() {
    return {
      events: [], // 存储从后端获取的事件数据
    };
  },
  mounted() {
    // 在组件挂载时调用后端 API
    this.fetchEvents();
  },
  methods: {
    // 获取事件列表
    fetchEvents() {
      axios.get('http://127.0.0.1:5000/events')
        .then(response => {
          this.events = response.data; // 将后端返回的数据存储到 events 中
        })
        .catch(error => {
          console.error('Error fetching events:', error);
        });
    },
  },
};
</script>

<template>
  <div>
    <h1>Events</h1>
    <ul>
      <li v-for="event in events" :key="event.id">
        {{ event.name }} - {{ event.date }} - {{ event.description }}
      </li>
    </ul>
  </div>
</template>

<style>
/* 添加一些简单的样式 */
form {
  margin-top: 20px;
}
form div {
  margin-bottom: 10px;
}
</style>