import { Component, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

const header = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin':'*'
}

@Component({
    selector: 'app-home-data',
    templateUrl: './home.component.html'
})

export class HomeComponent{
    private defaultURL: String = "http://127.0.0.1:5000/";
    
    constructor(private http: HttpClient, @Inject('BASE_URL') baseUrl: string) {
        this.logged(); //Kiểm tra đăng nhập   
    }

    public logged(){
        this.http.get<any>(this.defaultURL + 'logged', {headers: header}).subscribe(
            result => {
                var res: any = result
                console.log(res)
            },
            error => {
               //Todo
               alert(error)
            });
    }
}   
