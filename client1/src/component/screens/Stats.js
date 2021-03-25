import React, { useEffect, useState ,useContext} from 'react';
import {UserContext} from "../../App"
import axios from 'axios'
const List=()=>{
const [dataa,setData]=useState([])

    useEffect(()=>{
        fetch("/stats",{method: 'get'}).then(Response=>Response.json() 
        .then(data=>{
            setData(data)
        }))
     },[])
console.log(JSON.stringify(dataa));
const data=JSON.stringify(dataa, null, 1)
console.log(typeof(data));

return (
    <pre>{data}</pre>
  );

}

export default List;