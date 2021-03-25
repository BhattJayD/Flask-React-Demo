import React, { useEffect, useState ,useContext} from 'react';
import {UserContext} from "../../App"
import axios from 'axios'
const List=()=>{
const [dataa,setData]=useState([])

    useEffect(()=>{
        fetch("/count",{method: 'get'}).then(Response=>Response.json() 
        .then(data=>{
            setData(data)
        }))
     },[])
console.log(dataa);
    return(
        <div>
        <h5>Total Number Of battle is:- </h5>
        <h4 className="#880e4f pink darken-4" style={{width:"45px auro",color: "white"}}>{dataa.Total}</h4>
        </div>
    )
}
export default List;