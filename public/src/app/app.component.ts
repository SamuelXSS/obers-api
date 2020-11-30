import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

export interface PeriodicElement {
  name: string;
  position: number;
  weight: number;
  symbol: string;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  li: any;
  lis = [];
  input_value = '';
  title = 'cpf-validator';

  constructor(private http: HttpClient) {}

  onKey(event: any) {
    this.input_value = event.target.value;
  }

  public check(data: string): void {
    if (data.length <= 14) {
      this.http
        .post('http://localhost:9095/validator/Cpf', { cpf: data })
        .subscribe((Response) => {
          this.li = Response;
          this.lis = this.li;
        });
    } else {
      this.http
        .post('http://localhost:9095/validator/Cnpj', { cnpj: data })
        .subscribe((Response) => {
          this.li = Response;
          this.lis = this.li;
        });
    }
  }
  public checkSystem(): void {
    this.http
      .get('http://localhost:9095/health')
      .subscribe((Response) => {
        this.li = Response;
        this.lis = this.li;
      });
  }
}
