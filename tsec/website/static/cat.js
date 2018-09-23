/*// VUE COMPONENTS
Vue.component("img-card",{
    props:{
      imgTitle:{
        type:String,
        default:"Untitled"
      },
      imgLink:{
        type:String,
        default:"https://i.imgur.com/vt1Bu3m.jpg"
      },
      imgId:{
        type:Number,
        default:0
      },
      isSelected:Boolean
    },
    template:
    `<div class="card cursor-pointer" 
         v-on:click="$emit('imgClicked',{'imgId':imgId,'imgTitle':imgTitle})">
        <img class="card-img-top img-height-lock" :src="imgLink">
        <div class="card-body" v-bind:class="{'bg-primary':isSelected}">
          <h5 class="card-title" v-bind:class="{'text-white':isSelected}">
            {{imgTitle}}
          </h5>
    </div>
    </div>`
  });
  
  Vue.component("img-card-search",{
    props:{
      searchFunc:Function,
      maxResults:{
        type:Number,
        default:8
      }
    },
    data:function() {
      return {
        searchInputVal:"",
        resultPage:0,
        selectedItem:{}
      }
    },
    computed:{
      results:function() {
        var func = window[this.searchFunc];
        return func(this.searchInput,this.resultPage,this.maxResults);
      },
      searchInput:{
        get:function() {
          return this.searchInputVal;
        },
        set:function(val) {
          this.searchInputVal=val;
          this.resultPage=0;
        }
      },
      selectedId:function() {
        return this.selectedItem.imgId;
      }
    },
    methods:{
      canUsePrevious:function() {
        return this.resultPage>0;
      },
      previousPage:function() {
        if (this.resultPage>0) --this.resultPage;
      },
      nextPage:function() {
        ++this.resultPage;
      },
      onImgClicked:function(item) {
        this.selectedItem=item;
      }
    },
    template:
  `
  <div>
  <div class="form-group">
  <input v-model.lazy="searchInput" class="form-control"/>
  </div>
  
  <div class="no-overflow mb-2">
  <div class="float-left p-1">
    <button class="btn" v-on:click="previousPage" :disabled="!canUsePrevious()">Previous</button>
  </div>
  <div class="float-right p-1">
    <button class="btn" v-on:click="nextPage">Next</button>
  </div>
  </div>
  <div class="row">
    <div class="col-sm-3 form-group" v-for="result in results">
      <img-card 
        :imgTitle="result.imgTitle"
        :imgId="result.imgId"
        :isSelected="selectedId==result.imgId"
        v-on:imgClicked="onImgClicked"
      />
    </div>
  </div>
  
  <label>Selected: </label>
  <input class="form-control" type="text" readonly :value="selectedItem.imgTitle">
  
  </div>
  `
  });
  

  
  // GENERATE A BUNCH OF DATA FOR TESTING
  var bigData = [];
  
    bigData.push({
      imgId:1,
      imgTitle:numToWords(1)
    });
  bigData.push({
      imgId:2,
      imgTitle:"something"
    });
  bigData.push({
      imgId:3,
      imgTitle:"nothing"
    });
  bigData.push({
      imgId:4,
      imgTitle:"everything"
    });
  
  
  // SEARCH LOGIC
  var fakeSearchFunc = function(searchString,resultPage,maxResults) {
    if (searchString=="bad") return[];
    let filtered = bigData.filter(
    elem=> elem.imgTitle.toLowerCase().
      includes(
      searchString.toLowerCase()
      )
    );
    let a = [];
    let i=resultPage*maxResults;
    while (a.length<maxResults && i<filtered.length) {
      a.push(filtered[i]);
      ++i;
    }
    return a;
  };
  
  var vv = new Vue({el:"#vue-root"});
*/

