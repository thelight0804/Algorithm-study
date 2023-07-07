/*
Date:
  2023.07.07
Title:
  Find k'th smallest number by heap
Author:
  thelight0804
*/

class MinHeap{
    constructor(){
        this.heap = [];
    }
    add(val){
        this.heap.push(val);
        this.bubbleUp(this.heap.length - 1); //sort minimum
    }
    bubbleUp(idx) {
        while (idx > 0) {
            const parentIdx = Math.floor((idx - 1) / 2); //get parent index

            if (this.heap[parentIdx] > this.heap[idx]) { //sort
            this.swap(idx, parentIdx); //Bubble sort
            idx = parentIdx; //set now index
            }
        }
    }
    
    swap(idx1, idx2){ //Bubble sort
        var temp = this.heap[idx1];
        this.heap[idx1] = this.heap[idx2];
        this.heap[idx2] = temp;
    }

    pop(){ //return minimum value
        var item = this.heap[0];
        this.heap[0] = this.heap.pop(); //Last node goes to roof
        this.heapifyDown(0); //sort minimum
        return item;
    }

    heapifyDown(idx){
        //get left and child index
        var leftChildIdx = (2 * idx) + 1;
        var rightChildIdx = (2 * idx) + 2;
        
        while(this.heap[idx] > this.heap[leftChildIdx] || this.heap[idx] > this.heap[rightChildIdx]){
        if(this.heap[idx] > this.heap[leftChildIdx]){ //go to left down
            this.swap(idx, leftChildIdx);
            idx = leftChildIdx;
        }
        if(this.heap[idx] > this.heap[rightChildIdx]){ //go to right down
            this.swap(idx, rightChildIdx);
            idx = rightChildIdx;
        }
        //update index
        leftChildIdx = (2 * idx) + 1;
        rightChildIdx = (2 * idx) + 2;
        }
    }
}

heap = new MinHeap();

//add number
heap.add(9);
heap.add(7);
heap.add(5);
heap.add(3);
heap.add(1);

console.log(heap.heap); //[ 1, 3, 7, 9, 5 ]

for(var i = 0; i < 3; i++){
    console.log(heap.pop()); //1 3 5
}

console.log(heap.heap); //[ 7, 9 ]