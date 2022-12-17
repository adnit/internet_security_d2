<script>
import axios from "axios";
export default {
  data() {
    return {
      urlToLookup: "",
      info: "",
      reqResult: "",
    };
  },
  methods: {
    fetchData() {
      let config = {
        headers: {
          Accept: "*/*",
        },
      };

      let data = {
        url: this.urlToLookup,
      };
      axios.post("http://127.0.0.1:80/ping", data, config).then((response) => {
        this.reqResult = response.data.join(' ');
        document.getElementById('reqResult').disabled = true;
      });
    },
  },
};
</script>

<template>
  <div class="flex space-x-2 justify-center">
    <section class="h-screen">
      <div class="px-6 h-full text-gray-800">
        <div
          class="
            flex
            xl:justify-center
            lg:justify-between
            justify-center
            items-center
            flex-wrap
            h-full
            g-6
          "
        >
          <div
            class="
              grow-0
              shrink-1
              md:shrink-0
              basis-auto
              xl:w-6/12
              lg:w-6/12
              md:w-9/12
              mb-12
              md:mb-0
            "
          >
            <img
              src="https://fiek.uni-pr.edu/images/logosmall.png"
              alt="Sample image"
              style="width: 20%; margin: auto"
            />
            <textarea
              style="margin-top: 3%"
              v-model="reqResult"
              class="w-full"
              rows="15"
              id="reqResult"
            ></textarea>
          </div>
          <div class="xl:ml-20 xl:w-5/12 lg:w-5/12 md:w-8/12 mb-12 md:mb-0">
              <div
                class="
                  flex
                  items-center
                  my-4
                  before:flex-1
                  before:border-t
                  before:border-gray-300
                  before:mt-0.5
                  after:flex-1 after:border-t after:border-gray-300 after:mt-0.5
                "
              >
                <p class="text-center font-semibold mx-4 mb-0">
                  Shkruaj URL per DNS Lookup
                </p>
              </div>
              <div class="mb-3 xl:w-96 items-center">
                <label
                  for="exampleURL0"
                  class="form-label inline-block mb-2 text-gray-700"
                  >URL input</label
                >
                <input
                  type="text"
                  v-model="urlToLookup"
                  class="
                    form-control
                    block
                    w-full
                    px-3
                    py-1.5
                    text-base
                    font-normal
                    text-gray-700
                    bg-white bg-clip-padding
                    border border-solid border-gray-300
                    rounded
                    transition
                    ease-in-out
                    m-0
                    focus:text-gray-700
                    focus:bg-white
                    focus:border-blue-600
                    focus:outline-none
                  "
                  placeholder="URL input"
                />
              </div>
              <div class="text-center lg:text-left">
                <button
                  @click="fetchData()"
                  type="button"
                  class="
                    inline-block
                    px-7
                    py-3
                    bg-blue-600
                    text-white
                    font-medium
                    text-sm
                    leading-snug
                    uppercase
                    rounded
                    shadow-md
                    hover:bg-blue-700 hover:shadow-lg
                    focus:bg-blue-700
                    focus:shadow-lg
                    focus:outline-none
                    focus:ring-0
                    active:bg-blue-800 active:shadow-lg
                    transition
                    duration-150
                    ease-in-out
                  "
                >
                  Lookup
                </button>
              </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
</style>