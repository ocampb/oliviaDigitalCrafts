//Algo Friday

const array1 = [];
const array2 = [];

const algo = function () {
  const index1 = array1.length;
  const newarray1 = array1.sort();
  const newarray2 = array2.sort();
  const index2 = index1 - 1;
  if (newarray1[index2] > newarray2[index2]) {
    const newarraycontrol = newarray1;
  } else {
    const newarraycontrol = newarray2;
  }
  console.log(newarraycontrol);
  //   for (let i = 0; i < index2; i++) {

  //   }
};

algo();
