import { Component, Inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-home-data',
    templateUrl: './home.component.html'
})

export class HomeComponent{
    constructor(private http: HttpClient, @Inject('BASE_URL') baseUrl: string) {
    
    }
}   
