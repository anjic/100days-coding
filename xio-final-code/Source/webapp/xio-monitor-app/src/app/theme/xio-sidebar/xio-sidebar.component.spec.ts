import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { XioSidebarComponent } from './xio-sidebar.component';
import { MaterialModule } from '@angular/material';


describe('XioSidebarComponent', () => {
  let component: XioSidebarComponent;
  let fixture: ComponentFixture<XioSidebarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      imports: [ MaterialModule ],
      declarations: [ XioSidebarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(XioSidebarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
