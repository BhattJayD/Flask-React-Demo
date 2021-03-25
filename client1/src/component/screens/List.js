import React, { useEffect, useState ,useContext} from 'react';
import {UserContext} from "../../App"
import axios from 'axios'
const List=()=>{
const [dataa,setData]=useState([])

    useEffect(()=>{
        fetch("/list",{method: 'get'}).then(Response=>Response.json() 
        .then(data=>{
            setData(data)
        }))
     },[])
console.log(dataa);
const data=JSON.stringify(dataa, null, 1)
console.log(typeof(data));

return (
    <pre>{data}</pre>
  );

}

export default List;