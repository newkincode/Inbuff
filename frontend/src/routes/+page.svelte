<script>
	import { onMount } from 'svelte';
  
	let message = "hello";
  
	function fetchData() {
	  fetch("http://127.0.0.1:8000/return")
		.then((response) => response.json())
		.then((json) => {
		  if (message !== json.message) {
			message = json.message;
			console.log(json.message);
		  }
		  // 데이터를 가져온 후 다시 fetchData 함수 호출
		  fetchData();
		});
	}
  
	onMount(() => {
	  fetchData(); // 페이지 로드 시 최초 데이터 가져오기
	});
  </script>
  
  <h1>{message}</h1>
  