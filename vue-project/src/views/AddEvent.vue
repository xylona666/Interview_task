<template>
  <div>
    <h1>Events</h1>
    <!-- 显示事件列表 -->
    <ul>
      <li v-for="event in events" :key="event.id">
        {{ event.name }} - {{ event.date }} - {{ event.description }}
      </li>
    </ul>

    <h2>Add New Event</h2>
    <!-- 添加事件的表单 -->
    <form @submit.prevent="addEvent">
      <div>
        <label for="name">Event Name:</label>
        <input type="text" id="name" v-model="newEvent.name" required />
      </div>
      <div>
        <label for="date">Event Date:</label>
        <input type="date" id="date" v-model="newEvent.date" required />
      </div>
      <div>
        <label for="description">Description:</label>
        <textarea id="description" v-model="newEvent.description" required></textarea>
      </div>
      <button type="submit">Add Event</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      events: [], // 存储从后端获取的事件数据
      newEvent: {
        name: '',
        date: '',
        description: '',
      }, // 存储新事件的数据
    };
  },
  mounted() {
    // 获取事件列表
    this.fetchEvents();
  },
  methods: {
    // 获取事件列表
    fetchEvents() {
      axios.get('http://127.0.0.1:5000/events')
        .then(response => {
          this.events = response.data;
        })
        .catch(error => {
          console.error('Error fetching events:', error);
        });
    },
    // 添加新事件
    addEvent() {
      axios.post('http://127.0.0.1:5000/add-event', this.newEvent)
        .then(response => {
          alert(response.data.message); // 显示成功消息
          this.fetchEvents(); // 重新获取事件列表
          // 清空表单
          this.newEvent.name = '';
          this.newEvent.date = '';
          this.newEvent.description = '';
        })
        .catch(error => {
          console.error('Error adding event:', error);
        });
    },
  },
};
</script>

<style>
/* 添加一些简单的样式 */
form {
  margin-top: 20px;
}
form div {
  margin-bottom: 10px;
}
</style>