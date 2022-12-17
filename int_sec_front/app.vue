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

      axios
        .post("http://127.0.0.1:80/ping", data, config)
        .then((response) => {
          this.reqResult = response.data.join(" ");
          document.getElementById("reqResult").disabled = true;
        })
        .catch((error) => {
          this.reqResult = "Ka ndodhur nje problem"
        });
    },
  },
};
</script>

<template>
  <div class="justify-center bg-gray-900">
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
              alt="UP LOGO"
              class="w-1/4 mx-auto mb-8"
            />

            <form v-on:submit.prevent="fetchData">
              <label
                for="search"
                class="block mb-1 text-sm font-medium text-white"
                >URL</label
              >
              <div class="relative">
                <div
                  class="
                    absolute
                    inset-y-0
                    left-0
                    flex
                    items-center
                    pl-3
                    pointer-events-none
                  "
                >
                  <svg
                    aria-hidden="true"
                    class="w-5 h-5 text-gray-400"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                    xmlns="http://www.w3.org/2000/svg"
                  >
                    <path
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      stroke-width="2"
                      d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
                    ></path>
                  </svg>
                </div>
                <input
                  type="search"
                  id="search"
                  v-model="urlToLookup"
                  class="
                    block
                    w-full
                    p-4
                    pl-10
                    text-sm
                    border border-gray-600
                    rounded-lg
                    bg-gray-700
                    focus:ring-blue-500 focus:border-blue-500
                    placeholder-gray-400
                    text-white
                    focus:ring-blue-500 focus:border-blue-500
                  "
                  placeholder="ex. google.com"
                  required
                />

                <button
                  type="submit"
                  class="
                    text-white
                    absolute
                    right-2.5
                    bottom-2.5
                    focus:ring-4 focus:outline-none
                    font-medium
                    rounded-lg
                    text-sm
                    px-4
                    py-2
                    bg-blue-600
                    hover:bg-blue-700
                    focus:ring-blue-800
                  "
                >
                  Lookup
                </button>
              </div>
            </form>

            <label
              for="reqResult"
              class="block mb-1 mt-3 text-sm font-medium text-white"
              >DNS Lookup results</label
            >
            <textarea
              id="reqResult"
              v-model="reqResult"
              rows="15"
              disabled
              class="
                block
                p-2.5
                w-full
                text-sm
                rounded-lg
                border border-gray-300
                focus:ring-blue-500 focus:border-blue-500
                bg-gray-700
                border-gray-600
                placeholder-gray-400
                text-white
                focus:ring-blue-500 focus:border-blue-500
              "
              placeholder=""
            ></textarea>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
</style>