import { Component, Inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Title } from '@angular/platform-browser';
import { Router, ActivatedRoute } from "@angular/router";

const header = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin':'*'
}
@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css'] //Dùng file css ở đây, không dùng ở thẻ <head>
})

export class LoginComponent {
    private defaultURL: String = "http://127.0.0.1:5000/";
    returnUrl: string;
    user: any = {
        userName: "test",
        password: "123456"
    }
    data: any ={
        userName: "sdadafn",
        password: "123456",
        firstName: "123456",
        lastName: "123456",
        identityCard: "123456",
        phoneNumber: "123456",
        birthDay: "2020-01-01",
        gender: "Nam",
        address: "123456",
        note: "123456"
    }
    
    public constructor(private http: HttpClient, @Inject('BASE_URL') baseUrl: string
        , private titleService: Title, private router: Router, private route?: ActivatedRoute) {
        this.setTitle(); //Đưa lên phương thức khởi tạo
         
    }

    //Title phải set ở đây, không được set trong thẻ <title>
    public setTitle() {
        this.titleService.setTitle("Đăng nhập");
    }
   

    public validateUser(){
        // fetch(this.defaultURL + "validate-user", {
        //     method: 'post',
        //     headers: {
        //         'Content-Type': 'application/json',
        //         'Access-Control-Allow-Origin':'*'
        //     }, 
        //     body: JSON.stringify(this.user)
        // }).then(res => res.json()).then(data => console.info(data)).catch(err => console.error(err))
        // console.log(JSON.stringify(this.user));
        this.http.post(this.defaultURL + 'validate-user',
         JSON.stringify(this.user), {headers: header}).subscribe(
            result => {
                var res: any = result
                if(res.success){
                    console.log(result)
                    alert("Bạn đã đăng nhập thành công.")
                    this.router.navigate(['/']);
                }
                else{
                    alert("Tài khoản hoặc mật khẩu không đúng.")
                }
            },
            error => {
               //Todo
               alert(error)
            });
    }
}